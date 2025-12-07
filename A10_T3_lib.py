import sys

def readValues(PFilename: str, PValues: list[int]) -> None:
    try:
        with open(PFilename, "r", encoding="UTF-8") as file:
            for line in file:
                line = line.strip()
                if line != "":
                    try:
                        PValues.append(int(line))
                    except ValueError:
                        print(f"Error: Cannot convert '{line}' to integer.")
                        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: File '{PFilename}' not found.")
        sys.exit(1)
    return None

def displayValues(PLabel: str, PFilename: str, PValues: list[int]) -> None:
    joined = ", ".join(str(v) for v in PValues)
    print(f"{PLabel} '{PFilename}' -> {joined}")
    return None

def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    n = len(PValues)
    for Iteration in range(n - 1):
        Remaining = n - Iteration - 1
        for CurrentIndex in range(Remaining):
            NextIndex = CurrentIndex + 1
            Left = PValues[CurrentIndex]
            Right = PValues[NextIndex]
            if PAsc:
                SwapNeeded = Left > Right
            else:
                SwapNeeded = Left < Right
            if SwapNeeded:
                PValues[CurrentIndex], PValues[NextIndex] = (
                    PValues[NextIndex],
                    PValues[CurrentIndex],
                )
    return None