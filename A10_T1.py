########################################################
# Task A10_T1
# Developer Arttu Eklund
# Date 2025-12-03
########################################################

def readFile(Pfilename):
    values = []
    with open(Pfilename, "r", encoding="UTF-8") as file:
        for line in file:
            line = line.strip()
            if line:
                values.append(line)
    return values

def printVertical(Pvalues) -> None:
    print("# --- Vertically --- #")
    for v in Pvalues:
        print(v)
    print("# --- Vertically --- #")

def printHorizontal(Pvalues) -> None:
    print("# --- Horizontally --- #")
    print(", ".join(Pvalues))
    print("# --- Horizontally --- #")

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    values = readFile(filename)
    printVertical(values)
    printHorizontal(values)
    print("Program ending.")

if __name__ == "__main__":
    main()