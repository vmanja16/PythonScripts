# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from calculator import *

class CalculatorConsumer(QMainWindow, Ui_Calculator):

    def __init__(self, parent=None):
        super(CalculatorConsumer, self).__init__(parent)
        self.setupUi(self)

        self.output = "0."
        self.sum = 0
        self.buffer = ""
        self.number1 = None
        self.number2 = None
        self.operator = None
        self.digit = False
        self.onClear()
        self.btn0.clicked.connect(lambda:self.onDigit(0))
        self.btn1.clicked.connect(lambda:self.onDigit(1))
        self.btn2.clicked.connect(lambda:self.onDigit(2))
        self.btn3.clicked.connect(lambda:self.onDigit(3))
        self.btn4.clicked.connect(lambda:self.onDigit(4))
        self.btn5.clicked.connect(lambda:self.onDigit(5))
        self.btn6.clicked.connect(lambda:self.onDigit(6))
        self.btn7.clicked.connect(lambda:self.onDigit(7))
        self.btn8.clicked.connect(lambda:self.onDigit(8))
        self.btn9.clicked.connect(lambda:self.onDigit(9))
        self.btnPlus.clicked.connect(lambda:self.onOperator("ADD"))
        self.btnDivide.clicked.connect(lambda:self.onOperator("DIV"))
        self.btnMultiply.clicked.connect(lambda:self.onOperator("MULT"))
        self.btnMinus.clicked.connect(lambda:self.onOperator("SUB"))
        self.btnEqual.clicked.connect(self.onEqual)
        self.btnClear.clicked.connect(self.onClear)
        self.btnDot.clicked.connect(self.onDot)
        self.chkSeparator.stateChanged.connect(self.onChk)
        self.cboDecimal.currentIndexChanged.connect(self.onDec)
    def onDec(self):
        if self.digit:
            self.display(self.output)
        else:
            self.display(self.number1)
    def onChk(self):
        self.display(str(self.output).replace(",", ""))
    def onDot(self):
        if "." in self.buffer:return
        if not self.buffer:
            self.buffer = "0."
        else:
            self.buffer += "."
        self.digit = True
        self.display(self.buffer)
    def operate(self, a = None, b = None):
        if self.operator == "ADD":
            self.sum = a + b
        if self.operator == "MULT":
            self.sum = a * b
        if self.operator == "DIV":
            self.sum = a / b
        if self.operator == "SUB":
            self.sum = a - b
        self.operator = None
        self.number1 = self.sum
    def onDigit(self, digit):
        self.digit = True
        if self.buffer == "0" and not digit:
            digit = ""
        self.buffer += str(digit)
        self.display(float(self.buffer))
    def onOperator(self, operator):
        if self.number1:
            if self.digit:
                self.operate(self.number1, float(self.buffer))
                self.display(self.number1)
                self.operator = operator
            else:
                self.operator = operator
        if not self.number1:
            self.number1 = float(self.buffer) if self.buffer else 0.0
            self.operator = operator
        self.digit = 0
        self.buffer = ""
    def onClear(self):
        self.sum = 0
        self.number1 = None
        self.number2 = None
        self.digit = False
        self.buffer=""
        self.display(0.)
        self.operator = None
    def display(self, input=None):
        if input == None:
            if not self.buffer:
                input = 0
            else:
                input = self.buffer
        inputStr = str(input).replace(",", "")[:12]

        lhs = inputStr.split(".")[0]
        if "." in inputStr:
            rhs = inputStr.split(".")[1]
        else:
            rhs = ""
        output = ""
        if self.chkSeparator.isChecked():
            if len(lhs) < 4:
                output = lhs
            else:
                count = 0
                for num in lhs[::-1]:
                    if count == 0:
                        output = num+output
                        count += 1
                        continue
                    if (count) % 3 == 0:
                        output = num + "," + output
                    else:
                        output = num + output
                    count += 1
        else:
            output = lhs

        dec = self.cboDecimal.currentIndex()
        rhs = rhs[:dec][::-1].zfill(dec)[::-1]

        output += "." + rhs




        self.output = output
        self.txtDisplay.setText(QtGui.QApplication.translate("Calculator", str(output)[:12], None, QtGui.QApplication.UnicodeUTF8))
    def onEqual(self):
        if  self.number1 == None: return
        if not self.operator: return
        if not self.digit: return
        self.number2 = float(self.buffer)
        self.operate(self.number1, self.number2)
        self.digit = False
        self.buffer = ""
        self.display(self.number1)
    def printVariables(self):
        print("------------------------------")
        print("Number1 = %s" % str(self.number1))
        print("Number2 = %s" % str(self.number2))
        print("Sum = %s" % str(self.sum))
        print("Operator = %s" % str(self.operator))
        print("Digit? = %s" % str(self.digit))
        print("Buffer = %s" % str(self.buffer))
currentApp = QApplication(sys.argv)
currentForm = CalculatorConsumer()
currentForm.show()
currentApp.exec_()
