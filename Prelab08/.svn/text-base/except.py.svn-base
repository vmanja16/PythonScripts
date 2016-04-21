#! /usr/bin/env python3.4

def exception():
    val = input("Please enter some values: ")
    valList = val.strip().split()

    floatList=[]

    for i in valList:
        try:
            floatList.append(float(i))
        except ValueError:
            pass
    SUM = sum(floatList)

    print("The sum is %.1f" % SUM)

if __name__ == "__main__":
    exception()