__author__ = 'Vikram'

def addNumbers(num):
    num - int(num)
    sum = 0
    for i in range (num+1):
        sum += i
    return sum

def addMultiplesOf(num):
    num = int(num)
    multiplesList = []
    i = 1
    while (i * num) <= 1000:
        multiplesList.append(i*num)
        i += 1
    return sum(multiplesList)

def getNumberFrequency(digit):

    digit = str(digit)
    String = (
    "The value of Pi is 3 . 1 4 1 5 9 2 6 5 3 5 8 9 7 9 \
    3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5 0 2 8 8 4 1 9 7 1 \
    6 9 3 9 9 3 7 5 1 0 5 8 2 0 9 7 4 9 4 4 5 9 2 3 0 7 \
    8 1 6 4 0 6 2 8 6 2 0 8 9 9 8 6 2 8 0 3 4 8 2 5 3 4 \
    2 1 1 7 0 6 7 9 8 2 1 4 8 0 8 6 5 1 3 2 8 2 3 0 6 6 \
    4 7 0 9 3 8 4 4 6 0 9 5 5 0 5 8 2 2 3 1 7 2 5 3 5 9 \
    4 0 8 1 2 8 4 8 1 "
    )

    frequency = 0
    for i in String:
        if i == str(digit):
            frequency +=1
    return frequency

def getDigitalSum(input):
    Sum = 0
    for i in input:
        if i in [' ', '']:
            continue
        Sum += int(i)
    return Sum

def getSequenceWithoutDigit(digit):
    strList = ["736925233695599303035509581762617623184956190649483967300203776387436934399982",

    "943020914707361894793269276244518656023955905370512897816345542332011497599489",

    "627842432748378803270141867695262118097500640514975588965029300486760520801049",

    "153788541390942453169171998762894127722112946456829486028149318156024967788794",

    "981377721622935943781100444806079767242927624951078415344642915084276452000204",

    "276947069804177583220909702029165734725158290463091035903784297757265172087724",

    "474095226716630600546971638794317119687348468873818665675127929857501636341131"]

    string = ''.join(strList)
    digit = str(digit)
    strList = string.split(digit)
    maxLen = 0
    returnIndex = 0

    for index, item in enumerate(strList):
        if len(item) > maxLen:
            maxLen = len(item)
            returnIndex = index

    return strList[returnIndex]

def capitalizeMe(string):
    strList = string.split()
    for index, string in enumerate(strList):
        string = string[0].upper() + string[1:]
        strList[index] = string[:-1] + string[-1].upper()
    return ' '.join(strList)

