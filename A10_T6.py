########################################################
# Task A10_T6
# Developer Arttu Eklund
# Date 2025-12-07
########################################################

import copy
import time
from typing import Callable

def readValues(PValues: list[int]) -> str:
    PValues.clear()
    filename = input("Insert dataset filename: ")
    try:
        with open(filename, "r", encoding="UTF-8") as file:
            for line in file:
                line = line.strip()
                if line != "":
                    PValues.append(int(line))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return ""
    return filename

def bubbleSort(PNums: list[int]) -> list[int]:
    n = len(PNums)
    for i in range(n - 1):
        remaining = n - i - 1
        for j in range(remaining):
            if PNums[j] > PNums[j + 1]:
                PNums[j], PNums[j + 1] = PNums[j + 1], PNums[j]
    return PNums

def quickSort(PNums: list[int]) -> list[int]:
    if len(PNums) <= 1:
        return PNums
    pivot = PNums[len(PNums) // 2]
    left = [x for x in PNums if x < pivot]
    middle = [x for x in PNums if x == pivot]
    right = [x for x in PNums if x > pivot]

    return quickSort(left) + middle + quickSort(right)

def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    StartTime = time.perf_counter_ns()
    PSortingAlgorithm(PArr)
    EndTime = time.perf_counter_ns()
    return EndTime - StartTime

def saveResults(filename: str, results: list[str]) -> None:
    with open(filename, "w", encoding="UTF-8") as file:
        for line in results:
            file.write(line + "\n")

def printMenu() -> None:
    print("Options:")
    print("1 - Read dataset values")
    print("2 - Measure speeds")
    print("3 - Save results")
    print("0 - Exit")

def main() -> None:
    Values: list[int] = []
    Results: list[str] = []
    DatasetName: str = ""
    print("Program starting.")
    while True:
        print()
        printMenu()
        choice = input("Your choice: ")
        if choice == "0":
            print("Exiting program.")
            break
        elif choice == "1":
            DatasetName = readValues(Values)
        elif choice == "2":
            if not Values:
                print("No dataset loaded.")
                continue
            print(f"Measured speeds for dataset '{DatasetName}':")
            BuiltinTime = measureSortingTime(sorted, copy.deepcopy(Values))
            print(f" - Built-in sorted {BuiltinTime} ns")
            BubbleTime = measureSortingTime(bubbleSort, copy.deepcopy(Values))
            print(f" - Bubble sort {BubbleTime} ns")
            QuickTime = measureSortingTime(quickSort, copy.deepcopy(Values))
            print(f" - Quick sort {QuickTime} ns")
            Results.clear()
            Results.append(f"Measured speeds for dataset '{DatasetName}':")
            Results.append(f" - Built-in sorted {BuiltinTime} ns")
            Results.append(f" - Bubble sort {BubbleTime} ns")
            Results.append(f" - Quick sort {QuickTime} ns")
            Results.append("")
        elif choice == "3":
            if not Results:
                print("No results to save.")
                continue
            filename = input("Insert results filename: ")
            saveResults(filename, Results)
        else:
            print("Unknown choice. Try again.")
    Values.clear()
    Results.clear()
    print()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()