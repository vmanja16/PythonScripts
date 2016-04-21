#
#
#
#

import os
import glob
def rowSumIsValid(mat):
    if mat:
        SUM = sum(mat[0])
    for eachList in mat:
        if sum(eachList) != SUM:
            return False
    return True

def columnSumIsValid(mat):
    if not mat:
        return True
    Sums = []
    for element in mat[0]:
        Sums.append(0)
    for row in mat:
        for index, number in enumerate(row):
            Sums[index]+= number
    SUM = Sums[0]
    for i in Sums:
        if i != SUM:
            return False
    return True

def magicSquareIsValid(filePath):
    if not os.path.isfile(filePath):
        return None
    matrix=[]
    with open(filePath, 'r') as square:
        for line in square.readlines():
            row = line.strip().split()
            for index, i in enumerate(row):
                row[index] = int(i)
            matrix.append(row)
    if not columnSumIsValid(matrix) or not rowSumIsValid(matrix):
        return False
    return True

def getTotalCost(itemSet):
    CPUQuantityDict=dict(itemSet)
    returnDict={}
    fileList = glob.glob(os.path.join(os.getcwd(), "Stores", "*"))
    for file in fileList:
        SUM = 0
        Store = os.path.basename(file).split('.')[0]
        CPUPriceDict={}
        with open(file, 'r') as text:
            for line in text.readlines()[3:]:
                CPU = line.split(",")[0].strip()
                price = line.split(",")[-1].strip().strip('$')
                CPUPriceDict[CPU] = float(price)
            for CPU in CPUQuantityDict:
                SUM+= CPUPriceDict[CPU] * CPUQuantityDict[CPU]
        SUM = round(SUM,2)
        returnDict[Store]=SUM
    return returnDict

def getBestPrices(cpuSet):
    fileList = glob.glob(os.path.join(os.getcwd(), "Stores", "*"))
    returnDict={}
    for CPU in cpuSet:
        minPrice = 10000000
        minStore=""
        for file in fileList:
            with open(file, 'r') as text:
                Store = os.path.basename(file).split('.')[0]
                for line in text.readlines()[3:]:
                    eachCPU = line.split(",")[0].strip()
                    price = line.split(",")[-1].strip().strip('$')
                    price = float(price)
                    if CPU == eachCPU:
                        if price < minPrice:
                            minPrice = price
                            minStore=Store
        returnDict[CPU] = (minPrice, minStore)
    return returnDict

def getMissingItems():
    fileList = glob.glob(os.path.join(os.getcwd(), "Stores", "*"))
    storeCPUDict={}
    returnDict={}
    for file in fileList:
        with open(file, 'r') as text:
            Store = os.path.basename(file).split('.')[0]
            CPUList=[]
            for line in text.readlines()[3:]:
                CPU = line.split(",")[0].strip()
                CPUList.append(CPU)
            storeCPUDict[Store]=CPUList
    TotalList= []
    for eachList in storeCPUDict.values():
        for eachCPU in eachList:
            if eachCPU not in TotalList:
                TotalList.append(eachCPU)

    for key in storeCPUDict:
        tempList=[]
        for eachCPU in TotalList:
            if eachCPU not in storeCPUDict[key]:
                tempList.append(eachCPU)
        returnDict[key]=set(tempList)

    return returnDict



if __name__ == "__main__":
    pass