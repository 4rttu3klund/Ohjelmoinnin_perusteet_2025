########################################################
# Task A10_T3
# Developer Arttu Eklund
# Date 2025-12-03
########################################################

import sys
from A10_T3_lib import readValues, displayValues, bubbleSort

def main() -> None:
    Values: list[int] = []
    Filename = ""
    print("Program starting.")
    if len(sys.argv) == 2:
        Filename = sys.argv[1]
    else:
        Filename = input("Insert filename: ")
    readValues(Filename, Values)
    displayValues("Raw", Filename, Values)
    ValuesAsc = Values.copy()
    bubbleSort(ValuesAsc, True)
    displayValues("Ascending", Filename, ValuesAsc)
    ValuesDesc = Values.copy()
    bubbleSort(ValuesDesc, False)
    displayValues("Descending", Filename, ValuesDesc)
    Values.clear()

if __name__ == "__main__":
    main()