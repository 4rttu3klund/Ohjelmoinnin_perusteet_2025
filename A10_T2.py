########################################################
# Task A10_T2
# Developer Arttu Eklund
# Date 2025-12-03
########################################################

import sys

def readValues(PFilename: str, PValues: list[int]) -> None:
    try:
        with open(PFilename, "r", encoding="UTF-8") as file:
            for line in file:
                line = line.strip()
                if line != "":
                    try:
                        value = int(line)
                        PValues.append(value)
                    except ValueError:
                        print(f"Error: Cannot convert '{line}' to integer.")
                        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: File '{PFilename}' not found.")
        sys.exit(1)
    return None

def sumOfValues(PValues: list[int]) -> int:
    Sum = 0
    for v in PValues:
        Sum += v
    return Sum

def productOfValues(PValues: list[int]) -> int:
    Product = 1
    for v in PValues:
        Product *= v
    return Product

def main() -> None:
    Values: list[int] = []
    print("Program starting.")
    filename = input("Insert filename: ")
    readValues(filename, Values)
    Sum = sumOfValues(Values)
    Product = productOfValues(Values)
    print("# --- Sum of numbers --- #")
    print(Sum)
    print("# --- Sum of numbers --- #")
    print("# --- Product of numbers --- #")
    print(Product)
    print("# --- Product of numbers --- #")
    Values.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()