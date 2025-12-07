def readValues(filename: str) -> list[float]:
    values: list[float] = []
    File = open(filename, "r")
    for line in File:
        line = line.strip()
        if line != "":
            values.append(float(line))
    return values

def calculateSum(values: list[float]) -> float:
    return round(sum(values), 1)

def calculateAverage(values: list[float]) -> float:
    if len(values) == 0:
        return 0.0
    return round(sum(values) / len(values), 1)

def showOptions() -> None:
    print("Options:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")

def main() -> None:
    print("Program starting.")
    values: list[float] = []
    while True:
        showOptions()
        choice = input("Your choice: ")
        if not choice.isdigit():
            print("Unknown option!\n")
            continue
        choice = int(choice)
        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice == 1:
            filename = input("Insert filename: ")
            values = readValues(filename)
            print()
        elif choice == 2:
            print(f"Amount of values {len(values)}\n")
        elif choice == 3:
            print(f"Sum of values {calculateSum(values)}\n")
        elif choice == 4:
            print(f"Average of values {calculateAverage(values)}\n")
        else:
            print("Unknown option!\n")
    print("Program ending.")

if __name__ == "__main__":
    main()