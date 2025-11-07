def readValues(FileName):
    file = open(FileName, 'r', encoding="UTF-8")
    Values = []
    for line in file:
        value = line.strip()
        if value:
            Values.append(int(value))
    return Values

def analyseValues(Values):
    Count = len(Values)
    Sum = sum(Values)
    Greatest = max(Values)
    Avg = Sum / Count
    return f"Count;Sum;Greatest;Average\n{Count};{Sum};{Greatest};{Avg:.2f}\n"

def main():
    print("Program starting.")
    FileName = input("Insert filename: ")
    print("#### Number analysis - START ####")
    print(f'File "{FileName}" results:')
    Values = readValues(FileName)
    Analysis = analyseValues(Values)
    print(Analysis)
    print("#### Number analysis - END ####")
    print("Program ending.")

if __name__ == "__main__":
    main()