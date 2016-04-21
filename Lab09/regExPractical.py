import os, glob, re, sys

def getAddress(sentence):
    mac1  = re.compile(r"[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}")
    mac2  = re.compile(r"[A-Fa-f0-9]{2}-[A-Fa-f0-9]{2}-[A-Fa-f0-9]{2}-[A-Fa-f0-9]{2}-[A-Fa-f0-9]{2}-[A-Fa-f0-9]{2}")

    match1 = re.search(mac1,sentence)
    match2 = re.search(mac2,sentence)

    if match1:
        return match1.group()
    if match2:
        return match2.group()
    return None

def getSwitches(commandline):
    pattern = re.compile(r"\s*([\w+\\/:\.]+)\s*")
    matchlist = re.findall(pattern,commandline)
    operator = None
    returnList=[]
    print (matchlist)
    for index, element in enumerate(matchlist):
        element = element.strip()

        print(operator)
        if operator:
            if element.startswith("+"):
                operator = element.strip("+")
            elif element.startswith("\\"):
                operator = element.strip("\\")
            else:
                returnList.append((operator, element))


        if element.startswith("+"):
            operator = element.strip("+")
        elif element.startswith("\\"):
            operator = element.strip("\\")
        else:
            operator = None

        if operator:
            if operator.isupper():
                operator = None




    return sorted(returnList)

def getElements(fullAddress):
    if "_" in fullAddress:
        return None
    pattern = re.compile(r"http://(?P<base>[a-zA-z0-9\.]+)/(?P<controller>[a-zA-z0-9]+)/(?P<action>[a-zA-z0-9]+)$")
    pattern2 =re.compile(r"https://(?P<base>[a-zA-z0-9\.]+)/(?P<controller>[a-zA-z0-9]+)/(?P<action>[a-zA-z0-9]+)$")
    match = re.match(pattern, fullAddress)
    match1 = re.match(pattern2, fullAddress)
    if match:
        return (match.group("base"), match.group("controller"), match.group("action"))
    if match1:
        return (match1.group("base"), match1.group("controller"), match1.group("action"))

    return None

if __name__ == "__main__":
    print(getElements("http://www.purdue.edu/About_Us/History"))
