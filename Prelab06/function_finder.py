import os
import string
import glob
import sys
import re

pattern = r"def\s+(?P<function>[A-Za-z][\w-]*)\s*\((?P<args>.*)\)"

def fileCheck(file):
    if os.path.exists(file):
        if os.access(file, os.R_OK):
            return True
    print("Error: Could not read: noread")
    return False


def findFunction(inFile):
    if not fileCheck(inFile): return None
    with open(inFile, "r") as file:
        for line in file.readlines():
            match = re.search(pattern, line)
            if match:
                args=match.group("args")
                argList = args.strip().split(",")
                print(match.group("function"))
                for index, arg in enumerate(argList):
                    print("Arg" + str(index+1) + ":",
                          arg.strip())
if __name__ == "__main__":
    if len(sys.argv) == 2:
        fileList = glob.glob(os.path.join(os.getcwd(), sys.argv[1]))
        inFile = fileList[0]
        findFunction(inFile)
    else:
        print("Usage: function_finder.py <filename>")

