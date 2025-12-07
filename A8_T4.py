from A8_T4_lib import (
    MONTHS, WEEKDAYS,
    readTimestamps, calculateYears, calculateMonths, calculateWeekdays
)

def showOptions() -> None:
    print("Options:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    timestamps = []
    readTimestamps(filename, timestamps)
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
            year_str = input("Insert year: ")
            if year_str.isdigit():
                year = int(year_str)
                amount = calculateYears(year, timestamps)
                print(f"Amount of timestamps during year '{year}' is {amount}\n")
            else:
                print("Invalid year!\n")
        elif choice == 2:
            month = input("Insert month: ")
            amount = calculateMonths(month, timestamps)
            print(f"Amount of timestamps during month '{month}' is {amount}\n")
        elif choice == 3:
            weekday = input("Insert weekday: ")
            amount = calculateWeekdays(weekday, timestamps)
            print(f"Amount of timestamps during weekday '{weekday}' is {amount}\n")
        else:
            print("Unknown option!\n")
    print("Program ending.")

if __name__ == "__main__":
    main()