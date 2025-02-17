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

def printGrid(grid: list) -> None: 
    print("-------------------------")
    for i in range(9):
        st = ""
        for j in range(9):
            if(j % 3 == 0):
                st = st + "| " + str(grid[i][j]) + " "
            else:
                st = st + str(grid[i][j]) + " "
        st += "|"
        print(st)
        if i % 3 == 2:
            print("-------------------------")

def inRow(grid: list, value: int, row: int) -> bool:
    for i in range(len(grid)):
        if(grid[row][i] == value):
            return True
    return False

def inCol(grid: list, value: int, col: int) -> bool:
    for i in range(len(grid)):
        if(grid[i][col] == value):
            return True
    return False

def inBox(grid: list, value: int, row: int, col: int) -> bool:
    boxRow: int = row - row % 3
    boxCol: int = col - col % 3

    for i in range(boxRow, boxRow + 3):
        for j in range(boxCol, boxCol + 3):
            if grid[i][j] == value:
                return True
    return False

def CSP(grid:list) -> bool:
    size:int = len(grid)
    for row in range(size):
        for col in range(size):
            for value in (1, 10):
                if not inRow(grid, value, row) and not inCol(grid, value, col) and not inBox(grid, value, row, col):
                    grid[row][col] = value
                    if CSP(grid):
                        return True
                    else:
                        grid[row][col] = 0
            return False
    return True

def main() -> None:
    grid: list = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0 ,3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    printGrid(grid)
    print()
    if CSP(grid):
        print("Solved Using CSP")
        printGrid(grid)
    else:
        print("No Solution Found")




if __name__ == '__main__':
    main()
