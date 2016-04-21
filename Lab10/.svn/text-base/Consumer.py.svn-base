import sys

from PySide.QtGui import *
from BasicUI import *
import re

class Consumer(QMainWindow, Ui_MainWindow):

    states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        self.clearButton.clicked.connect(self.onClear)
        self.emailLineEdit.textChanged.connect(self.onEdit)
        self.lastNameLineEdit.textChanged.connect(self.onEdit)
        self.firstNameLineEdit.textChanged.connect(self.onEdit)
        self.zipLineEdit.textChanged.connect(self.onEdit)
        self.addressLineEdit.textChanged.connect(self.onEdit)
        self.stateLineEdit.textChanged.connect(self.onEdit)
        self.saveToTargetButton.clicked.connect(self.onSave)
        self.loadButton.clicked.connect(self.loadData)



        self.error = 0

    def onSave(self):
        List = [self.firstNameLineEdit, self.lastNameLineEdit, self.addressLineEdit, self.cityLineEdit, self.stateLineEdit, self.zipLineEdit, self.emailLineEdit]
        self.error = 0
        for index, obj in enumerate(List):
            if not obj.text():
                if index == 0:
                    self.emailError("First Name")
                if index == 1:
                    self.emailError("Last Name")
                if index == 2:
                    self.emailError("Address")
                if index == 3:
                    self.emailError("City")
                if index == 4:
                    self.emailError("State")
                if index == 5:
                    self.emailError("Zip")
                if index == 6:
                    self.emailError("Email")

        if self.stateLineEdit.text() not in self.states:
            self.emailError("State")
        if not re.match("[0-9]{5}", self.zipLineEdit.text()):
            self.emailError("Zip")
        if not re.match("\w+@\w+\.\w+", self.emailLineEdit.text()):
            self.emailError("Email")

        if self.error == 1:
            return

        self.errorInfoLabel.setText("")
        self.String = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
        self.String+= "<user>\n"
        self.String+= "\t<FirstName>%s</FirstName>\n" % self.firstNameLineEdit.text()
        self.String+= "\t<LastName>%s</LastName>\n" % self.lastNameLineEdit.text()
        self.String+= "\t<Address>%s</Address>\n" % self.addressLineEdit.text()
        self.String+= "\t<City>%s</City>\n" % self.cityLineEdit.text()
        self.String+= "\t<State>%s</State>\n" % self.stateLineEdit.text()
        self.String+= "\t<ZIP>%s</ZIP>\n" % self.zipLineEdit.text()
        self.String+= "\t<Email>%s</Email>\n" % self.emailLineEdit.text()
        self.String+= "</user>\n"

        with open("target.xml", "w") as f:
            f.write(self.String)
    def onLoad(self):
        pass

    def emailError(self, code):
        self.errorInfoLabel.setText("Error: %s is not valid!" % code)
        self.error = 1



    def onClear(self):
        self.firstNameLineEdit.setText("")
        self.lastNameLineEdit.setText("")
        self.cityLineEdit.setText("")
        self.stateLineEdit.setText("")
        self.addressLineEdit.setText("")
        self.zipLineEdit.setText("")
        self.emailLineEdit.setText("")
        self.saveToTargetButton.setEnabled(False)
        self.loadButton.setEnabled(True)

    def onEdit(self):
        self.saveToTargetButton.setEnabled(True)
        self.loadButton.setEnabled(False)


    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.

        *** This method is required for unit tests! ***
        """
        pattern = re.compile("<.*>(?P<data>.+)</.*>$")
        with open(filePath, "r") as file:
            List = [self.firstNameLineEdit, self.lastNameLineEdit, self.addressLineEdit, self.cityLineEdit, self.stateLineEdit, self.zipLineEdit, self.emailLineEdit]
            for obj in List:
                obj.setText("")
            for line in file.readlines():
                data = ""
                data = line.split(">")[1].split("<")[0]

                if "FirstName" in line:
                    self.firstNameLineEdit.setText(data)
                if "LastName" in line:
                    self.lastNameLineEdit.setText(data)
                if "Address" in line:
                    self.addressLineEdit.setText(data)
                if "City" in line:
                    self.cityLineEdit.setText(data)
                if "State" in line:
                    self.stateLineEdit.setText(data)
                if "ZIP" in line:
                    self.zipLineEdit.setText(data)
                if "Email" in line:
                    self.emailLineEdit.setText(data)

                self.loadButton.setEnabled(False)
                self.saveToTargetButton.setEnabled(True)

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)




if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
