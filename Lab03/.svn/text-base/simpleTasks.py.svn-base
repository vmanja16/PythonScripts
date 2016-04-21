#
#
# $Author$
# $Date$
# $HeadURL$
# $Revision$

def getPairwiseDifference(vec):
    if type(vec) != list:
        return None
    if not vec:
        return None
    diffVec=[]
    for index, item in enumerate(vec):
        if index +1 == len(vec):
            break
        diffVec.append(vec[index+1]-item)
    return diffVec

def flatten(l):
    if type(l) != list:
        return None
    for eachList in l:
        if type(eachList) != list:
            return None
    flattenedList=[]
    for eachList in l:
        flattenedList.extend(eachList)
    return flattenedList

def partition(l,n):
    bigList=[]
    if type(l) != list:
        return None
    if not l:
        return None
    index =0
    while index+n+1 <= len(l):
        tempList=[]
        tempList=l[index:index+n]
        bigList.append(tempList)
        index += n
    if index - len(l) < n:
        tempList=l[index:]
        bigList.append(tempList)


    return bigList

def rectifySignal(signal):
    if type(signal) != list:
        return None
    if not signal:
        return None
    outputList=[]
    for number in signal:
        if number < 0.0:
            number = 0
        outputList.append(number)
    return outputList

def floatRange(a, b, s):
    if a >=b:
        return None
    floatList=[]
    number=float(a)
    while number <= float(b):
        floatList.append(float(number))
        number+=s
        number = round(number,2)
    if b not in floatList:
        floatList.append(float(b))
    return floatList

def getLongestWord(s):
    if type(s) != str:
        return None
    if len(s.split())<2:
        return None
    max =0
    maxWord=""
    for word in  s.split():
        if len(word)>max:
            maxWord=word
            max=len(word)
    return maxWord

def decodeNumbers(numList):
    if type(numList) != list:
        return None
    for number in numList:
        if type(number) != int:
            return None
    decodedList=[chr(int(x)) for x in numList]
    return "".join(decodedList)

def getCreditCard(s):
    if not s:
        return None
    cardList=[]
    for element in s:
        if element in ["0","1","2","3","4","5","6","7","8","9"]:
            cardList.append(int(element))
    return cardList


if __name__ == '__main__':
    print(getPairwiseDifference([1,2,3]))
    print(flatten([[1,2,3],[4,5,6]]))
    print(partition([11,18,15,21,19,13,14,17], 3))
    print(rectifySignal([1.0,8.0,2.0,-1.0,-5.0]))
    print(floatRange(1,3,0.2))



