import os, sys, re, glob, string
from collections import Counter

def getFileDirectory(dir = None):
    """
    :return the files directory
    """
    if not dir:
        print 'No directory for files'
        return None
    try:
        filePath = os.path.join('C:\\', 'Users', 'Vikram','Desktop','PythonScripts', dir, dir)
    except (IOError,OSError, WindowsError) as details:
        raise details
    return filePath

def getWordFrequency():
    """
    :return: a dictionary of word: frequency across all files in folder 'files'
    """
    path = getFileDirectory('files')
    print path, '\n'
    files = glob.glob(os.path.join(path,'*'))
    frequencyCounter = Counter()
    text = ''

    # Compile text
    for file in files:
        text = open(file,"r").read()
        for char in text:
            if char in string.punctuation:
                text = text.replace(char, "")
        frequencyCounter.update(text.split())

    frequencyDict = dict(frequencyCounter.most_common())

    return frequencyDict

#Dictionary = getWordFrequency()
#for key in sorted(Dictionary.keys()):
#    print key, ": ", Dictionary[key]


def getDuplicates():
    """
    :return: Dictionary- key: filename, value:(wordcount, list of identical files]
    """
    path = getFileDirectory('files')
    files = glob.glob(os.path.join(path,'*'))
    files.sort()

    returnDict = {}
    fileStringList = []
    fileWordCountDict = {}

    for index, file in enumerate(files):
        tuple = ()
        tuple = (os.path.basename(os.path.splitext(file)[0]), open(file,"r").read())
        fileStringList.append(tuple)

    # Get file->contents dictionary
    fileStringDict = dict(fileStringList)

    # Get file->wordcount dictionary
    for file in fileStringDict:
        fileWordCountDict[file] = len(fileStringDict[file].split())

    # Create return dictionary
    fileList = fileStringDict.keys()
    for file in sorted(fileStringDict):
        if file not in fileList:
            continue
        groupKey = fileStringDict[file]
        duplicateList = []
        # Look for duplicates of group key string
        for possibleDuplicate in fileList:
            if groupKey == fileStringDict[possibleDuplicate]:
                duplicateList.append(possibleDuplicate)
                fileList.remove(possibleDuplicate)
        returnDict[file] = (fileWordCountDict[file], sorted(duplicateList))

    return returnDict


def getPurchaseReport():
    path = getFileDirectory('purchases')
    files = glob.glob(os.path.join(path,'*'))
    files.sort()


    file = glob.glob(os.path.join(path, 'Item List.txt'))[0]
    if file in files:
        files.remove(file)
    # Get item->price dictionary
    fp = open(file, 'r')

    pricePattern = re.compile('([\w]+)\s*\$(\d.\d\d)')
    itemPriceList = re.findall(pricePattern, fp.read())
    itemPriceDict = dict(itemPriceList)
    fp.close()

    filePriceDict = {}
    quantityPattern = re.compile('([\w]+)\s*([\d]+)')
    for file in files:
        fp = open(file, 'r')
        filename = int(os.path.basename(os.path.splitext(file)[0])[-3:])
        price = 0
        itemQuantityDict = dict( re.findall(quantityPattern, fp.read()) )
        for item in itemQuantityDict:
            price += float(itemPriceDict[item]) * int(itemQuantityDict[item])
        filePriceDict[filename] = price
        fp.close()

    return filePriceDict

def getTotalSold():
    path = getFileDirectory('purchases')
    files = glob.glob(os.path.join(path,'*'))
    files.sort()
    itemQuantityDict = {}
    quantityPattern = re.compile('([\w]+)\s*([\d]+)')
    for file in files:
        fp = open(file, 'r')
        tempdict = dict( re.findall(quantityPattern, fp.read()) )
        for item in tempdict:
            if item not in itemQuantityDict.keys():
                itemQuantityDict[item]= int(tempdict[item])
            else:
                itemQuantityDict[item] += int(tempdict[item])
        fp.close()

    return itemQuantityDict



















