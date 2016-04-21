#
# $Author$
# $Date$
# $HeadURL$
# $Revision$
# $Id$

import os
import sys
import glob
import math

def getAverage(inputList):
    SUM = sum(inputList)
    return SUM/float(len(inputList))

def getHeadAverage(inputList, n):
    list = inputList[:n]
    return sum(list)/float(n)

def getTailMax(inputList, n):
    list = inputList[:-n-1:-1]
    return max(list)

def getNumberAverage(inputList):
    intList = [int(x) for x in inputList]
    return sum(intList)/float(len(intList))

def getFormattedSSN(number):
    number = "{0:09d}".format(number)
    number = str(number)
    return "%s%s%s-%s%s-%s%s%s%s" % tuple([i for i in number])

def findName( l, s):
    for name in l:
        if s in name.split():
            return name
def getColumnSum(mat):
    Matrix=[]
    columnList=[]
    for column in mat[-1]:
        columnList.append(0)
    for index, row in enumerate(mat):
        for index, column in enumerate(row):
            columnList[index] += column
    return columnList

def getFormattedNames(ln):
    formattedList=[]
    for name in ln:
        formattedList.append('{}, {} {}.'.format(name[2], name[0], name[1]) )
    return formattedList

def getElementWiseSum(l1,l2):
    sumList=[]
    if (len(l2) < len(l1) ):
        temp=l1
        l1=l2
        l2=temp
    if len(l2)==0:
        return l1
    # assume l1 is smaller
    i = 0
    for number in l1:
        sumList.append(number+l2[i])
        i += 1
    sumList.extend(l2[i:])
    return sumList

def removeDuplicates(l):
    uniqueList=[]
    for i in l:
        if i not in uniqueList:
            uniqueList.append(i)
    return uniqueList

def getMaxOccurence(l):
    occurenceDict={}
    for number in l:
        if number in occurenceDict:
            occurenceDict[number] += 1
        else:
            occurenceDict[number] = 1
    maxVal = 0
    maxKey= 0
    for key in occurenceDict:
        if occurenceDict[key] > maxVal:
            maxVal = occurenceDict[key]
            maxKey = key
    return maxKey

def getMaxProduct(l):
    multipleList=[]
    for index, number in enumerate(l):
        if (index + 2 >= len(l)):break
        multipleList.append(number*l[index+1]*l[index+2])
    print(multipleList)
    maxProduct=max(multipleList)
    return maxProduct

if __name__ == '__main__':
    print(getAverage([1, 2, 3]))
    print(getHeadAverage([1,2,3],2))
    print(getTailMax([1,2,3,2,1,0], 4))
    print(getNumberAverage([1,2,"3"]))
    print(getFormattedSSN(123456789))
    print(findName(["john dorian", "what who"], "dorian"))
    print(getColumnSum([[1,2,3],[4,5,6]]))
    print(getFormattedNames([["James", "W", "Wasington"]]))
    print(getElementWiseSum([1,2,3,4],[1,2,3]))
    print(removeDuplicates([1,2,3,4,4,3,1,3,4,5,6,7,6,8,6]))
    print(getMaxOccurence([1,2,3,4,4,3,1,3,4,5,6,7,6,8,4]))
    print(getMaxProduct([1,2,3,4,5,6,1,2,3]))