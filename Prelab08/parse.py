#! /usr/bin/env python3.4
#
import sys,os

def fileCheck():
    if len(sys.argv) != 2:
        print("Usage: parse.py [filename]")
        return
    file = sys.argv[1]
    try:
        obj = open(file, 'r')
        obj.close()
        parse(file)
    except IOError:
        print("%s is not a readable file" % file)


def parse(file):
    with open(file, 'r') as text:
        for line in text.readlines():
            lineList = line.split()
            numList = []
            wordList = []
            for key in lineList:
                try:
                    numList.append(int(key))
                except ValueError:
                    wordList.append(key)
            if numList:
                avg = float(sum(numList)/len(numList))
                print("{0:.03f} {1}".format(avg, " ".join(wordList)) )
            else:
                print(" ".join(wordList))

if __name__ == "__main__":
    fileCheck()

