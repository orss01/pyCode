class Node():
    variables: list
    value: int
    box: int

    def __init__(self, value: int, box: int):
        self.variables = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.value = value
        self.box = box
        self.delete(self.value)
        if(value != 0):
            self.variables = []

    def getValue(self) -> int:
        return self.value
    
    def setValue(self, value: int) -> None:
        self.value = value
        self.variables = []
    
    def getVariables(self) -> list:
        return self.variables
    def delete(self, variable: int) -> None:
        if variable in self.variables:
            self.variables.remove(variable)
    def getBox(self) -> int:
        return self.box 
    def toString(self) -> str:
        return ("value: %d, box: %d, Variables: " % (self.value, self.box)) + str(self.variables)

# tempGrid1: list = grid.copy()
# tempGrid1[i][j].setValue(grid[i][j].getVariables()[0])
# tempGrid2: list = grid.copy()
# tempGrid2[i][j].setValue(grid[i][j].getVariables()[1])
# tempGrid1Solution: bool = CSP(tempGrid1)
# tempGrid2Solution: bool = CSP(tempGrid2)

l: list = []
l.append(Node(0,1))
l.append(Node(0,2))
l.append(Node(0,3))
t: list = l.copy()

t[0].setValue(l[0].getVariables()[0])

for i in range(len(l)):
    print("l: " + l[i].toString())
    print("t: " + t[i].toString())

