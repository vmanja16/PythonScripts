import re
import glob
import os
fileList = glob.glob(os.path.join(os.getcwd(),"Part2.in"))
inFile = fileList[0]
#print (inFile)

pattern = r"(?P<login>[\w\.-]+)@(?P<domain>purdue.edu)(?P<score>.+)"
def prepend():
    """
    if line is a plain purdue address, use .ecn.purdue.edu
    then print line with "/100" appended
    :return: None
    """
    with open(inFile, 'r') as file:
        for line in file.readlines():
            match = re.search(pattern,line)
            if match:
                print(match.group("login")+ "@ecn."+
                      match.group("domain")+
                      match.group("score")+
                      "/100"
                      )
            else:
                print(line.strip() + "/100")
                pass
    pass

if __name__ == "__main__":
    prepend()
