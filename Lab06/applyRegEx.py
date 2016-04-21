import glob
import re
import os

file = glob.glob(os.path.join(os.getcwd(), "SiteRegistration.txt"))[0]

def getRejectedUsers():
    rejectLastPattern =  re.compile(r"(?P<last>[\w]+)[,][\s](?P<first>[\w]+)[\s,;]*$")
    rejectFirstPattern = re.compile(r"(?P<first>[\w]+)\s(?P<last>[\w]+)[\s,;]*$")
    rejectList = []
    with open(file, 'r') as myFile:
        for line in myFile.readlines():
            match = rejectLastPattern.match(line)
            if match:
                rejectList.append(match.group("first").strip()+ " " + match.group("last").strip())
            match = rejectFirstPattern.match(line)
            if match:
                rejectList.append(match.group("first").strip() + " " + match.group("last").strip())
    return sorted(rejectList)

def getUsersWithEmails():
    emailLastPattern =  re.compile(r"(?P<last>[\w]+)[,][\s](?P<first>[\w]+).*,(?P<email>[\w\.-]+@[\w\.-]+).*$")
    emailFirstPattern = re.compile(r"(?P<first>[\w]+)\s(?P<last>[\w]+).*,(?P<email>[\w\.-]+@[\w\.-]+).*$")
    returnDict={}
    with open(file, 'r') as myFile:
        for line in myFile.readlines():
            match = emailLastPattern.match(line)
            if match:
                returnDict[match.group("first").strip()+ " " + match.group("last").strip()]=match.group("email").strip()
            match = emailFirstPattern.match(line)
            if match:
                returnDict[match.group("first").strip()+ " " + match.group("last").strip()]=match.group("email").strip()

    return returnDict

def getUsersWithPhones():
    nameLastPattern =  re.compile(r"(?P<last>[\w]+)[,][\s](?P<first>[\w]+).*$")
    nameFirstPattern = re.compile(r"(?P<first>[\w]+)\s(?P<last>[\w]+).*$")
    phonePattern = re.compile(r".*,(?P<number>(\d{10})|(\(\d{3}\)\s\d{3}-\d{4})|(\d{3}-\d{3}-\d{4})).*")
    returnDict={}
    with open(file, 'r') as myFile:
        for line in myFile.readlines():
            match = nameLastPattern.match(line)
            pmatch = phonePattern.match(line)
            if match:
                name = match.group("first").strip()+ " " + match.group("last").strip()
                if pmatch:
                    number = pmatch.group("number").strip()
                    if number[0]== "(":
                        returnDict[name] = number
                    else:
                        number = number.replace("-","")
                        number = "(" + number[:3] + ")" + " " + number[3:6] + "-" + number[6:]
                        returnDict[name] = number


            match = nameFirstPattern.match(line)
            if match:
                name = match.group("first").strip()+ " " + match.group("last").strip()
                if pmatch:
                    number = pmatch.group("number").strip()
                    if number[0]== "(":
                        returnDict[name] = number
                    else:
                        number = number.replace("-","")
                        number = "(" + number[:3] + ")" + " " + number[3:6] + "-" + number[6:]
                        returnDict[name] = number
       #             if(len(number)!= )
    return returnDict

def getUsers():
    nameLastPattern =  re.compile(r"(?P<last>[\w]+)[,][\s](?P<first>[\w]+).*$")
    nameFirstPattern = re.compile(r"(?P<first>[\w]+)\s(?P<last>[\w]+).*$")
    Users=[]
    with open(file, 'r') as myFile:
        for line in myFile.readlines():
            match = nameFirstPattern.match(line)
            if match:
                name = match.group("first").strip()+ " " + match.group("last").strip()
                Users.append(name)
            match = nameLastPattern.match(line)
            if match:
                name = match.group("first").strip()+ " " + match.group("last").strip()
                Users.append(name)
        return Users

def getUsersWithStates():
    nameLastPattern =  re.compile(r"(?P<last>[\w]+)[,][\s](?P<first>[\w]+).*$")
    nameFirstPattern = re.compile(r"(?P<first>[\w]+)\s(?P<last>[\w]+).*$")
    phonePattern = re.compile(r".*,(?P<number>\w[\w\s]+)$")
    returnDict={}
    with open(file, 'r') as myFile:
        for line in myFile.readlines():
            match = nameLastPattern.match(line)
            pmatch = phonePattern.match(line)
            if match:
                name = match.group("first").strip()+ " " + match.group("last").strip()
                if pmatch:
                    number = pmatch.group("number").strip()
                    returnDict[name] = number



            match = nameFirstPattern.match(line)
            if match:
                name = match.group("first").strip()+ " " + match.group("last").strip()
                if pmatch:
                    number = pmatch.group("number").strip()
                    returnDict[name] = number
    return returnDict


def getUsersWithoutEmails():
    users = getUsers()
    #userPhoneDict=getUsersWithPhones()
    rejectedUsers=getRejectedUsers()
    userEmailDict=getUsersWithEmails()
    validUsers=[]
    for user in users:
        if user not in rejectedUsers and user not in userEmailDict.keys():
            validUsers.append(user)
    return sorted(validUsers)

def getUsersWithoutPhones():
    users = getUsers()
    userPhoneDict=getUsersWithPhones()
    rejectedUsers=getRejectedUsers()
    #userEmailDict=getUsersWithEmails()
    validUsers=[]
    for user in users:
        if user not in rejectedUsers and user not in userPhoneDict.keys():
            validUsers.append(user)
    return sorted(validUsers)

def getUsersWithoutStates():
    users = getUsers()
    #userPhoneDict=getUsersWithPhones()
    rejectedUsers=getRejectedUsers()
    #userEmailDict=getUsersWithEmails()
    userStateDict=getUsersWithStates()
    validUsers=[]
    for user in users:
        if user not in rejectedUsers and user not in userStateDict.keys():
            validUsers.append(user)
    return sorted(validUsers)

def getUsersWithCompleteInfo():
    users = getUsers()
    userPhoneDict=getUsersWithPhones()
    rejectedUsers=getRejectedUsers()
    userEmailDict=getUsersWithEmails()
    userStateDict=getUsersWithStates()
    validUsers=[]
    returnDict={}
    for user in users:
        if user not in rejectedUsers and user in userStateDict.keys() and user in userPhoneDict.keys() and user in userEmailDict:
            validUsers.append(user)
    for user in validUsers:
        returnDict[user] = (userEmailDict[user], userPhoneDict[user], userStateDict[user])
    return returnDict
#print(getRejectedUsers())
#print(getUsersWithEmails())
#print(getUsersWithStates())