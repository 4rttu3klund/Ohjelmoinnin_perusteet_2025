from datetime import datetime

MONTHS = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)

WEEKDAYS = (
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"
)


def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
    """Reads timestamps from a text file into a list."""
    PTimestamps.clear()

    try:
        with open(PFilename, "r") as file:
            for line in file:
                line = line.strip()
                if line != "":
                    ts = datetime.strptime(line, "%Y-%m-%dT%H:%M")
                    PTimestamps.append(ts)
    except FileNotFoundError:
        print("File not found!")
    except ValueError:
        print("Invalid timestamp format in file!")


def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
    """Counts timestamps matching the given year."""
    return sum(1 for ts in PTimestamps if ts.year == PYear)


def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
    """Counts timestamps matching the given month name."""
    month_index = None

    # Normalize input to allow different cases
    for i, m in enumerate(MONTHS):
        if m.lower() == PMonth.lower():
            month_index = i + 1
            break

    if month_index is None:
        return 0

    return sum(1 for ts in PTimestamps if ts.month == month_index)


def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
    """Counts timestamps matching the given weekday name."""
    weekday_index = None

    for i, wd in enumerate(WEEKDAYS):
        if wd.lower() == PWeekday.lower():
            weekday_index = i
            break

    if weekday_index is None:
        return 0

    return sum(1 for ts in PTimestamps if ts.weekday() == weekday_index)