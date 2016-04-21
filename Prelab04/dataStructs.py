#
#
# $Author$
# $Date$
# $HeadURL$
# $Revision$

import os
import glob
import string
import pprint as pp

def getFileList():
    print(os.getcwd())
    return glob.glob(os.path.join(os.getcwd(),"files","*"))


def getWordFrequency():
    wordFrequencyDict={}
    punctuation = set(string.punctuation)
    fileList = getFileList()
    for file in fileList:
        with open(file, 'r') as text:
            output = "".join(text.readlines())
            for word in output.split():
                word = word.strip()
                word = ''.join(letter for letter in word if letter not in string.punctuation)
                if word in wordFrequencyDict:
                    wordFrequencyDict[word] += 1
                else:
                    wordFrequencyDict[word] = 1
    return wordFrequencyDict

def getDuplicates():
    valueDict={}
    basenames=[]
    fileList = getFileList()
    # get TEXT values
    for file in fileList:
        with open(file, 'r') as text:
            valueDict[os.path.basename(file).split(".")[0]] = "".join(text.readline())
    basenames = list(valueDict.keys())

    keyList=[]
    for file in valueDict.keys():
        if file not in basenames:
            continue
        value = valueDict[file]
        basenames.remove(file)
        templist=[file]
        for name in basenames:
            if valueDict[name] == value:
                templist.append(name)
                basenames.remove(name)
        keyList.append(sorted(templist))

    returnDict={}
    for eachList in keyList:
        groupKey = eachList[0]
        content = valueDict[groupKey]
        contents=[]
        for word in content.split():
            word = word.strip()
            word = ''.join(letter for letter in word if letter not in string.punctuation)
            contents.append(word)
        wordCount = len(set(contents))
        returnDict[groupKey] = (wordCount, eachList)
    return returnDict


def getPurchaseReport():
    itemFile = glob.glob(os.path.join(os.getcwd(), "purchases", "Item List.txt"))[0]
    itemPriceDict={}
    returnDict={}
    with open(itemFile, 'r') as input:
        for line in input.readlines()[2:]:
            line = line.strip().split()
            x= line[-1].strip("$")
            itemPriceDict[line[0].strip()]=float(x)

    for file in glob.glob(os.path.join(os.getcwd(), "purchases", "*")):
        if "Item List.txt" in file:continue
        with open(file, 'r') as input:
            sum = 0
            for line in input.readlines()[2:]:
                line = line.strip().replace("$", "").split()
                item = line[0]
                quantity = line[-1]
                if item not in itemPriceDict:
                    continue
                sum += float(itemPriceDict[item]) * int(quantity)
        returnDict[int(os.path.basename(file).split(".")[0].split("_")[-1])] = round(sum,2)
    return returnDict



def getTotalSold():
    itemQuantityDict={}
    for file in glob.glob(os.path.join(os.getcwd(), "purchases", "*")):
        if "Item List.txt" in file:continue
        with open(file, 'r') as input:
            for line in input.readlines()[2:]:
                line = line.strip().replace("$", "").split()
                item = line[0]
                quantity = int(line[-1])
                if item in itemQuantityDict:
                    itemQuantityDict[item] += quantity
                else:
                    itemQuantityDict[item] = quantity

    return itemQuantityDict

if __name__ == "__main__":
    pass
    #print(getFileList())
    #pp.pprint(getWordFrequency())
    #pp.pprint(getDuplicates())
    #pp.pprint(getPurchaseReport())