
import string, re

def idIsAcceptable(ver_id):
    for character in ver_id:
        if character in string.ascii_letters:continue
        if character in string.digits: continue
        if character == "_": continue
        return False
    return True

def processSingle(ver_assignment):

    pattern = ".(?P<portName>.+)\((?P<pinName>.+)\)"
    if not re.match(pattern, ver_assignment):
        raise ValueError(ver_assignment)
    reDict = re.match(pattern, ver_assignment).groupdict()
    if ver_assignment[0] != ".":
        raise ValueError(ver_assignment)
    if ver_assignment[-1] != ")":
        raise ValueError(ver_assignment)

    theList = ver_assignment.split("(")

    portName = reDict["portName"]
    pinName = reDict["pinName"]

    if not idIsAcceptable(portName):
        raise ValueError(ver_assignment)
    if not idIsAcceptable(pinName):
        raise ValueError(ver_assignment)


    return (portName, pinName)

def processLine(ver_line):
    theList = ver_line.strip().split()

    if not idIsAcceptable(theList[0].strip()):
        raise ValueError(ver_line)
    if not idIsAcceptable(theList[1].strip()):
        raise ValueError(ver_line)

    Line = "".join(theList[2:]).strip()

    if Line[0] != "(":
        raise ValueError(ver_line)

    if Line[-1] != ")":
        raise ValueError(ver_line)


    line = Line.lstrip("(")[:-1]
    assignmentList = line.split(",")
    newAssignmentList=[]
    for assignment in assignmentList:
        newAssignmentList.append(processSingle(assignment.strip()))
    return (theList[0], theList[1], tuple(newAssignmentList))





if __name__ == "__main__":
    pass
