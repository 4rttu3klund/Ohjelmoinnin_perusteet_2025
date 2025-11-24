def readFile(filename: str) -> list[str]:
    print(f'Reading file "{filename}".')
    Rows: list[str] = []
    File = open(filename, "r", encoding="UTF-8")
    next(File)
    for line in File:
        line = line.strip()
        if line:
            Rows.append(line)
    return Rows

def analyseTimestamps(Rows: list[str], Weekdays: tuple[str], Results: list[str]):
    print("Analysing timestamps.")
    for day in Weekdays:
        count = sum(1 for row in Rows if row.startswith(day))
        Results.append(f" - {day} {count} stamps")
    return None

def displayResults(results: list[str]):
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for line in results:
        print(line)
    print("### Timestamp analysis ###")
    return None

def main():
    print("Program starting.")
    Filename = input("Insert filename: ")
    Weekdays: tuple[str] = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    )
    Rows = readFile(Filename)
    if not Rows:
        print("No data rows to analyze.")
        print("Program ending.")
        return
    Results: list[str] = []
    analyseTimestamps(Rows, Weekdays, Results)
    displayResults(Results)
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()