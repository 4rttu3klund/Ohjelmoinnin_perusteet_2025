def analyseFile():
    Filename = input("Insert filename to read: ")
    print(f'Reading names from "{Filename}".')
    file = open(Filename, 'r', encoding="UTF-8")
    print("Analysing names...")
    names = []
    for line in file:
        name = line.strip()
        if name:
            names.append(name)
    Count = len(names)
    if Count == 0:
        ShortName = 0
        LongName = 0
        AvgName = 0.00
    else:
        Length = [len(n) for n in names]
        ShortName = min(Length)
        LongName = max(Length)
        AvgName = sum(Length) / Count
    print("Analysis complete!")
    print(f"#### REPORT BEGIN ####\nName count - {Count}\nShortest name - {ShortName} chars\nLongest name - {LongName} chars\nAverage name - {AvgName:.2f} chars\n#### REPORT END ####")
    return None

def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    analyseFile()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()