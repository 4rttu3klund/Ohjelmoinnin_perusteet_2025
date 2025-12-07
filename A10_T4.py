########################################################
# Task A10_T4
# Developer Arttu Eklund
# Date 2025-12-03
########################################################

import sys
from A10_T4_lib import mergeSort

def readValues(filename: str) -> list[int]:
    values: list[int] = []
    try:
        with open(filename, "r", encoding="UTF-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    values.append(int(line))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except ValueError:
        print("Error: Non-integer found in file.")
        sys.exit(1)
    return values

def listToString(values: list[int]) -> str:
    return ", ".join(str(v) for v in values)

def main() -> None:
    print("Program starting.")
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input("Insert filename: ")
    ValuesRaw = readValues(filename)
    print(f"Raw '{filename}' -> {listToString(ValuesRaw)}")
    ValuesAsc = ValuesRaw.copy()
    mergeSort(ValuesAsc, True)
    print(f"Ascending '{filename}' -> {listToString(ValuesAsc)}")
    ValuesDesc = ValuesRaw.copy()
    mergeSort(ValuesDesc, False)
    print(f"Descending '{filename}' -> {listToString(ValuesDesc)}")
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()