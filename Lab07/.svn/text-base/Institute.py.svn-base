#
#
#
#


class Simulation:
    def __init__(self, simnNo, simDate, chipName, chipCount, chipCost):
        self.simulationNumber = simnNo
        self.simulationDate = simDate
        self.chipName = chipName
        self.chipCount = chipCount
        self.chipCost = chipCost
        self.simulationCost = self.chipCount * chipCost

    def __str__(self):
        return "{0}: {1:03d}, {2}, ${3:06.2f}".format(self.chipName, self.simulationNumber, self.simulationDate, self.simulationCost)

class Employee:
    def __init__(self, employeeName, employeeID):
        self.employeeName = employeeName
        self.employeeID = employeeID
        self.simulationsDict = {}

    def addSimulation(self,sim):
        self.simulationsDict[sim.simulationNumber] = sim

    def getSimulation(self,simNo):
        return self.simulationsDict.get(simNo)

    def __str__(self):
        return "{0}, {1}: {2:02d} Simulations".format(self.employeeID, self.employeeName, len(self.simulationsDict.keys()))

    def getWorkload(self):
        text = []
        text.append(self.__str__())
        text2=[]
        for key in self.simulationsDict:
            text2.append(str(self.simulationsDict[key]))
        text2.sort()
        text = text.extend(text2)
        return (self.__str__()+"\n" + "\n".join(text2))


    def addWorkload(self, fileName):
        with open(fileName, 'r') as file:
            for line in file.readlines()[2:]:
                line = line.strip().split()
                self.simulationsDict[int(line[0].strip())] = Simulation(int(line[0]), line[1], line[2], int(line[3]), float(line[4].strip("$")))


class Facility:
    def __init__(self, facilityName):
        self.facilityName = facilityName
        self.employeesDict = {}

    def addEmployee(self, employee):
        self.employeesDict[employee.employeeName] = employee

    def getEmployees(self, *args):
        return [self.employeesDict[arg] for arg in args]


    def __str__(self):
        s = "{0}: {1:02d} Employees\n".format(self.facilityName, len(self.employeesDict.keys()))
        l = []
        for key in self.employeesDict:
            l.append(str(self.employeesDict[key]))
        l.sort()
        return (s + "\n".join(l))

    def getSimulation(self, simNo):
        for employee in self.employeesDict:
            for simulation in self.employeesDict[employee].simulationsDict:
                if simulation == simNo:
                    return self.employeesDict[employee].simulationsDict[simulation]
        return None

if __name__ == "__main__":
    pass