########################################################
# Task A10_T7
# Developer Arttu Eklund
# Date 2025-12-07
########################################################

import random
random.seed(1234)

def layMines(PMineField: list[list[int]], PMines: int):
    rows = len(PMineField)
    cols = len(PMineField[0])
    placed = 0
    while placed < PMines:
        r = random.randrange(rows)
        c = random.randrange(cols)
        if PMineField[r][c] != 9:
            PMineField[r][c] = 9
            placed += 1

def calculateNearbys(PMineField: list[list[int]]) -> None:
    rows = len(PMineField)
    cols = len(PMineField[0])
    for r in range(rows):
        for c in range(cols):
            if PMineField[r][c] == 9:
                continue
            count = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < rows and 0 <= cc < cols:
                        if PMineField[rr][cc] == 9:
                            count += 1
            PMineField[r][c] = count

def generateMinefield(PMineField: list[list[int]], PRows: int, PCols: int, PMines: int) -> None:
    PMineField.clear()
    for _ in range(PRows):
        PMineField.append([0] * PCols)
    layMines(PMineField, PMines)
    calculateNearbys(PMineField)

def printBoard(board):
    if not board:
        print("No board generated.")
        return
    for row in board:
        print(row)

def saveBoard(board, filename):
    with open(filename, "w", encoding="UTF-8") as f:
        for row in board:
            line = ",".join(str(x) for x in row)
            f.write(line + "\n")

def main() -> None:
    print("Program starting.")
    minefield = []
    while True:
        print("\nOptions:")
        print("1 - Generate minesweeper board")
        print("2 - Show generated board")
        print("3 - Save generated board")
        print("0 - Exit")
        choice = input("Your choice: ")
        if choice == "1":
            rows = int(input("Insert rows: "))
            cols = int(input("Insert columns: "))
            mines = int(input("Insert mines: "))
            generateMinefield(minefield, rows, cols, mines)
        elif choice == "2":
            printBoard(minefield)
        elif choice == "3":
            if not minefield:
                print("No board generated.")
            else:
                filename = input("Insert filename: ")
                saveBoard(minefield, filename)
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")
    print("\nProgram ending.")

if __name__ == "__main__":
    main()