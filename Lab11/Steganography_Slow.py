import zlib, base64, numpy as np, re, copy
class Payload:
    def __init__(self,img = None, compressionLevel=-1, xml=None):
        if not xml and img == None:
            raise ValueError("No image or xml provided")
        if compressionLevel < -1 or compressionLevel > 9:
            raise ValueError("Invalid compression level")
        self.compressionLevel = compressionLevel
        self.img = img
        self.xml = xml
        if not self.xml:
            if type(img) != np.ndarray:
                raise TypeError("Invalid image type")
            cpy = copy.deepcopy(self.img)
            self.rawData = cpy.flatten()
            self.generateXML()
        elif self.img == None:
            if type(xml) != str:
                raise TypeError("Invalid xml type")
            self.generateImage()
    def generateImage(self):
        pattern = re.compile(r'.*type=\"(?P<type>.*)\".*size=\"'
                             r'(?P<size>.*)\".*ssed=\"'
                             r'(?P<compression>.*)\"')
        match = pattern.search(self.xml)
        if match:
            Type = match.group("type")
            compressed = match.group("compression")
            rowcol = match.group("size").strip("(").strip(")")
            row = int(rowcol.split(",")[0].strip())
            col = int(rowcol.split(",")[1].strip())
            data = re.search(r">\n(?P<data>.+)\n</payload>", self.xml)
            if data:
                data = data.group("data")
            data = base64.b64decode(data)
            if compressed == "True":
                data = zlib.decompress(data)
            sep = int(len(data)/3)
            if Type == "Color":
                r = data[:sep]
                g = data[sep:sep*2]
                b = data[sep*2:]
                data = [list(tup) for tup in zip(r,g,b)]
            else:
                data = list(data)
            # turn data into matrix of tuples
            newdata = [list(data[i:i+col]) for i in range(0, len(data), col)]
            arr = np.array(newdata)
            self.img = arr
    def generateXML(self):
        data = []
        if self.img.ndim == 2:
            color = "Gray"
            for i in self.rawData:
                data.append(i)
        else:
            color = "Color"
            for i in range(0,3):
                data.extend(self.rawData[i::3])
        data = bytes(data)
        if self.compressionLevel == -1:
            compressed = False
        else:
            compressed = True
            data = zlib.compress(data, int(self.compressionLevel))
        data = base64.b64encode(data)
        rows = str(self.img.shape[0])
        cols = str(self.img.shape[1])
        self.xml =  '<?xml version="1.0" encoding="UTF-8"?>\n'
        self.xml += '<payload type="%s" ' % color
        self.xml += 'size="%s,%s" compressed="%s">\n' % (
                rows, cols, compressed )
        self.xml += (data.decode("ascii") )+ "\n"
        self.xml += "</payload>"
class Carrier:
    def __init__(self, img):
        if type(img) != np.ndarray:
            raise TypeError("Invalid image")
        self.img = img # DO NOT MODIFY self.img
        self.cpy = copy.deepcopy(self.img)
        self.start = b'<?xml version="1.0" encoding="UTF-8"?>'
    def payloadExists(self):
        data = self.cpy.flatten()
        if self.img.ndim == 2:
            byteGroup = self.extractGrey(data[:304])
        else:
            byteGroup = self.extractColor(data[:912])
        if self.start == byteGroup[:len(self.start)]:
            return True
        else:
            return False
    def clean(self):
        im = self.cpy.flatten()
        col = self.img.shape[1]
        if self.img.ndim == 3:
                data = ([(a&~1,b&~1,c&~1) for (a,b,c) in zip(im[0::3], im[1::3], im[2::3])])
        else:
            data = [b & ~1 for b in im]
        newData = [list(data[i:i+col]) for i in range(0, len(data), col)]
        return np.array(newData)
    def embedErrorCheck(self, payload, override):
        if type(payload) != Payload:
            raise TypeError("Invalid payload")
        if self.payloadExists() and not override:
            raise Exception("Current carrier already contains payload")
        bitsAvailable = self.img.shape[0] * self.img.shape[1]
        if self.img.ndim == 3:
            bitsAvailable *= 3
        bytesReq = (payload.img.shape[0] * payload.img.shape[1] + 105) # 105 for xml header, 8 to convert bytes->bits
        if payload.img.ndim == 3:
            bytesReq *=3
        bitsReq = bytesReq * 8
        if bitsReq > bitsAvailable:
            raise ValueError("Payload is too large to embed in carrier")
    def embedPayload(self, payload, override=False):
        self.embedErrorCheck(payload, override)
        pdata = payload.xml.encode("ascii")
        cdata = self.cpy.flatten()
        newData=[]
        if self.img.ndim == 3:
            for i in range(3):
                newData.extend(cdata[i::3])
        else:
            newData = cdata

        bitList = []
        for eachByte in pdata:
            for i in range(8)[::-1]:
                bitList.append((eachByte>>i) & 1)
        final = []
        for index, byte in enumerate(newData):
            if index in range(len(bitList)):
                final.append( (byte & ~1) | bitList[index])
            else:
                final.append(byte)

        if self.img.ndim == 3:
            sep = int(len(newData)/3)
            r = final[:sep]
            g = final[sep:sep*2]
            b = final[sep*2:]
            final = [list(tup) for tup in zip(r,g,b)]

        col = self.img.shape[1]
        newData = [list(final[i:i+col]) for i in range(0, len(final), col)]
        arr = np.array(newData, dtype=np.uint8)
        return arr
    def extractPayload(self):
        if not self.payloadExists():
            raise Exception("Payload does not exist for carrier")
        data = self.cpy.flatten()
        if self.img.ndim == 2:
            byteGroup = self.extractGrey(data)
        else:
            byteGroup = self.extractColor(data)
        pattern = re.compile(b'<\?xml version="1\.0" encoding="UTF-8"\?>\n.*\n.*\n</payload>')
        match = pattern.search(byteGroup)
        if match:
            return Payload(xml=match.group().decode("ascii"))
    def extractColor(self,data):
        singleList=[]
        for i in range(0,3):
            singleList.extend(data[i::3])
        return(self.extractGrey(singleList))
    def extractGrey(self, data):
        bitList = []
        for byte in data:
            bitList.append(byte & 0b1)
        count = 0
        byteList = []
        newByte = 0
        for integer in bitList:
            if count > 1 and count % 8 ==0:
                count = 0
                byteList.append(newByte)
                newByte = 0
            newByte = newByte | (integer << (7-count))
            count += 1
        byteList.append(newByte)
        byteGroup = bytes(byteList)
        return byteGroup
if __name__ == "__main__":
    pass