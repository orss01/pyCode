# -------------------------
# | 0 0 0 | 0 0 0 | 0 0 0 |
# | 0 0 0 | 0 0 0 | 0 0 0 |
# | 0 0 0 | 0 0 0 | 0 0 0 |
# -------------------------
# | 0 0 0 | 0 0 0 | 0 0 0 |
# | 0 0 0 | 0 0 0 | 0 0 0 |
# | 0 0 0 | 0 0 0 | 0 0 0 |
# -------------------------
# | 0 0 0 | 0 0 0 | 0 0 0 |
# | 0 0 0 | 0 0 0 | 0 0 0 |
# | 0 0 0 | 0 0 0 | 0 0 0 |
# -------------------------

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

def makeNode(i:int, num: int, grid: list, box: int) -> None:
    if num != 0:
        grid[i].append(Node(num, box))
    else:
        grid[i].append(Node(0, box))

def getGrid() -> list:
    grid: list = []

    for i in range(9):
        print("Enter Row " + str(i + 1) + " (0 if blank)")
        grid.append([])
        uInput = input()
        validLength: bool = False
        validInput: bool = False
        while not validLength or not validInput:
            validLength = True
            validInput = True
            if len(uInput) < 9:
                validLength = False
                print("Not enough numbers, re-enter Row " + str(i + 1) + " (0 if blank)")
                uInput = input()
            else:
                for c in range(9):
                    if ord(uInput[c]) < 48 or ord(uInput[c]) > 57:
                        validInput = False
                if(not validInput):
                    print("Not valid numbers, re-enter Row " + str(i + 1) + " (0 if blank)")
                    uInput = input()

        for j in range(9):
            num: int = ord(uInput[j]) - 48
            if i < 3 and j < 3:
                makeNode(i, num, grid, 1)
            elif i < 3 and j < 6:
                makeNode(i, num, grid, 2)
            elif i < 3 and j < 9:
                makeNode(i, num, grid, 3)
            elif i < 6 and j < 3:
                makeNode(i, num, grid, 4)
            elif i < 6 and j < 6:
                makeNode(i, num, grid, 5)
            elif i < 6 and j < 9:
                makeNode(i, num, grid, 6)
            elif i < 9 and j < 3:
                makeNode(i, num, grid, 7)
            elif i < 9 and j < 6:
                makeNode(i, num, grid, 8)
            elif i < 9 and j < 9:
                makeNode(i, num, grid, 9)
    return grid

def printGrid(grid: list) -> None: 
    print("-------------------------")
    for i in range(9):
        st = ""
        for j in range(9):
            if(j % 3 == 0):
                st = st + "| " + str(grid[i][j].getValue()) + " "
            else:
                st = st + str(grid[i][j].getValue()) + " "
        st += "|"
        print(st)
        if i % 3 == 2:
            print("-------------------------")


def CSP(grid: list) -> bool:
    done: bool = False
    count: int = 0
    while not done and count < 1000:
        count += 1
        done = True
        for i in range(9):
            for j in range(9):
                if grid[i][j].getValue() == 0:
                    done = False
                    if len(grid[i][j].getVariables()) == 1:
                        grid[i][j].setValue(grid[i][j].getVariables()[0])
                else:
                    node: Node = grid[i][j]
                    for k in range(9):
                        if k != i:
                            grid[k][j].delete(node.getValue())
                        if k != j:
                            grid[i][k].delete(node.getValue())
                    if node.getBox() == 1:
                        for n in range(3):
                            for m in range(3):
                                if n != i and m != j:
                                    grid[n][m].delete(node.getValue())
                    elif node.getBox() == 2:
                        for n in range(3):
                            for m in range(3, 6):
                                if n != i and m != j:
                                    grid[n][m].delete(node.getValue())
                    elif node.getBox() == 3:
                        for n in range(3):
                            for m in range(6, 9):
                                if n != i and m != j:
                                    grid[n][m].delete(node.getValue())
                    elif node.getBox() == 4:
                        for n in range(3, 6):
                            for m in range(3):
                                if n != i and m != j:
                                    grid[n][m].delete(node.getValue())
                    elif node.getBox() == 5:
                        for n in range(3, 6):
                            for m in range(3, 6):
                                if n != i and m != j:
                                    grid[n][m].delete(node.getValue())
                    elif node.getBox() == 6:
                        for n in range(3, 6):
                            for m in range(6, 9):
                                if n != i and m != j:
                                    grid[n][m].delete(node.getValue())
                    elif node.getBox() == 7:
                        for n in range(6, 9):
                            for m in range(3):
                                if n != i and m != j:
                                    grid[n][m].delete(node.getValue())
                    elif node.getBox() == 8:
                        for n in range(6, 9):
                            for m in range(3, 6):
                                if n != i and m != j:
                                    grid[n][m].delete(node.getValue())
                    elif node.getBox() == 9:
                        for n in range(6, 9):
                            for m in range(6, 9):
                                if n != i and m != j:
                                    grid[n][m].delete(node.getValue())
    return done


def main() -> None:
    grid = getGrid()
    solution: bool = CSP(grid)
    if solution:
        printGrid(grid)
    else:
        print("No Solution Found")
    
    for i in range(9):
        for j in range(9):
            print(grid[i][j].toString())


if __name__ == '__main__':
    main() 