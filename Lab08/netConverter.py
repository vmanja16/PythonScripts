from HardwareTasks import *


def verilog2vhdl(ver_line):
    try:
        Args = processLine(ver_line)
    except:
        return "Error: Bad Line."

    instance = Args[1]
    Comp = Args[0]
    pairList = []
    for pair in Args[2]:
        pairList.append(pair[0]+"=>"+pair[1])
    assignments = ", ".join(pairList)
    return instance + ": " + Comp + " PORT MAP(" + assignments + ");"

def convertNetlist(sourceFile, targetFile):
    retList = []
    with open(sourceFile, "r") as text:
        for line in text.readlines():
            retList.append(verilog2vhdl(line))
    with open(targetFile, "w") as target:
        target.write("\n".join(retList))


if __name__ == "__main__":
    pass
