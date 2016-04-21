#
#
# $Author$
# $Date$
# $HeadURL$
# $Revision$

import os
import string
import glob

def getStudentIdDict():
    studFile = glob.glob(os.path.join(os.getcwd(), "files", "students.txt"))[0]
    idStudentDict = {}
    with open(studFile, "r") as myFile:
        for line in myFile.readlines()[2:]:
            student = line.strip().split("|")[0].strip()
            ID = line.strip().split("|")[-1].strip()
            idStudentDict[student] = ID
    return idStudentDict

def getIdStudentDict():
    studFile = glob.glob(os.path.join(os.getcwd(), "files", "students.txt"))[0]
    idStudentDict = {}
    with open(studFile, "r") as myFile:
        for line in myFile.readlines()[2:]:
            student = line.strip().split("|")[0].strip()
            ID = line.strip().split("|")[-1].strip()
            idStudentDict[ID] = student
    return idStudentDict

def getDetails():
    fileList = glob.glob(os.path.join(os.getcwd(), "files", "EE*"))
    studentIdDict = getStudentIdDict()
    returnDict={}
    for student in studentIdDict.keys():
        studentList=[]
        for file in fileList:
            if file == "students.txt":continue
            course = os.path.basename(file)[4:7]
            with open(file, "r") as text:
                for line in text.readlines()[2:]:
                    id = line.strip().split()[0].strip()
                    grade = int(line.strip().split()[-1].strip())
                    if id == studentIdDict[student]:
                        tuple=(course, grade)
                        studentList.append(tuple)
        returnDict[student] = set(studentList)
    return returnDict


def getStudentList(classNumber):
    idstudentDict = getIdStudentDict()
    file = glob.glob(os.path.join(os.getcwd(), "files", "*%s*"% classNumber))
    returnList=[]
    if not file:
        return []
    else:
        file = file[0]

    with open(file, "r") as text:
        for line in text.readlines()[2:]:
            id = line.strip().split()[0].strip()
            student = idstudentDict[id]
            returnList.append(student)
    return sorted(returnList)

def searchForName(studentName):
    detailDict=getDetails()
    if not studentName in detailDict.keys():
        return {}
    return dict(detailDict[studentName])

def searchForID(studentID):
    idStudentDict=getIdStudentDict()
    if studentID not in idStudentDict:
        return {}
    return searchForName(idStudentDict[studentID])

def findScore(studentName, classNumber):
    file = glob.glob(os.path.join(os.getcwd(), "files", "*%s*"% classNumber))
    if not file:
        return None
    else:
        file = file[0]
    StudentIdDict=getStudentIdDict()
    if studentName not in StudentIdDict:
        return None

    scoreDict=searchForName(studentName)
    return scoreDict[classNumber]

def getHighest(classNumber):
    file = glob.glob(os.path.join(os.getcwd(), "files", "*%s*"% classNumber))
    if not file:
        return ()
    else:
        file = file[0]
    idGradeDict={}
    idStudentDict=getIdStudentDict()
    with open(file, "r") as text:
        for line in text.readlines()[2:]:
            id = line.strip().split()[0].strip()
            grade = int(line.strip().split()[-1].strip())
            idGradeDict[id] = grade
    maxGrade = 0
    maxId=""
    for id in idGradeDict:
        if idGradeDict[id] > maxGrade:
            maxGrade = idGradeDict[id]
            maxId = id
    name = idStudentDict[maxId]
    return (name, float(maxGrade))

def getLowest(classNumber):
    file = glob.glob(os.path.join(os.getcwd(), "files", "*%s*"% classNumber))
    if not file:
        return ()
    else:
        file = file[0]
    idGradeDict={}
    idStudentDict=getIdStudentDict()
    with open(file, "r") as text:
        for line in text.readlines()[2:]:
            id = line.strip().split()[0].strip()
            grade = int(line.strip().split()[-1].strip())
            idGradeDict[id] = grade
    minGrade = 1000
    minId=""
    for id in idGradeDict:
        if idGradeDict[id] < minGrade:
            minGrade = idGradeDict[id]
            minId = id
    name = idStudentDict[minId]
    return (name, float(minGrade))



def getAverageScore(studentName):
    studentIdDict=getStudentIdDict()
    if studentName not in studentIdDict.keys():
        return None
    scoreDict = searchForName(studentName)
    length = len(list(scoreDict.values()))
    return sum(scoreDict.values()) /float(length)


if __name__ == "__main__":
    print(getDetails())