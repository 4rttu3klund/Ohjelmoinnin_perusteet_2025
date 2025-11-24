DELIMITER = ";"

class TIMESTAMP:
    def __init__(self):
        self.weekday = ""
        self.hour = ""
        self.consumption = 0.0
        self.price = 0.0

class DAILY_USAGE:
    def __init__(self, weekday: str):
        self.weekday = weekday
        self.daily_usage = 0.0
        self.daily_cost = 0.0

def readTimestamps(filename: str):
    print(f'Reading file "{filename}".')
    timestamps: list[TIMESTAMP] = []
    File = open(filename, "r", encoding="UTF-8")
    next(File)
    for line in File:
        row = line.strip()
        if not row:
            continue
        columns = row.split(DELIMITER)
        if len(columns) < 4:
            continue
        ts = TIMESTAMP()
        ts.weekday = columns[0]
        ts.hour = columns[1]
        ts.consumption = float(columns[2])
        ts.price = float(columns[3])
        timestamps.append(ts)
        columns.clear()
    return timestamps

def dailyUsage(timestamps: list[TIMESTAMP],
                        weekdays: tuple[str],
                        analysis: list[DAILY_USAGE],
                        results: list[str]):
    print("Analysing timestamps.")
    for day in weekdays:
        analysis.append(DAILY_USAGE(day))
    for ts in timestamps:
        for usage in analysis:
            if ts.weekday == usage.weekday:
                usage.daily_usage += ts.consumption
                usage.daily_cost += ts.consumption * ts.price
    for usage in analysis:
        results.append(
            f" - {usage.weekday} usage {usage.daily_usage:.2f} kWh, "
            f"cost {usage.daily_cost:.2f} €"
        )
    return None

def displayResults(results: list[str]):
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for line in results:
        print(line)
    print("### Electricity consumption summary ###")
    return None

def main():
    print("Program starting.")
    Filename = input("Insert filename: ")
    Weekdays = (
        "Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturnday", "Sunday"
    )
    Timestamps = readTimestamps(Filename)
    Analysis: list[DAILY_USAGE] = []
    Results: list[str] = []
    dailyUsage(Timestamps, Weekdays, Analysis, Results)
    displayResults(Results)
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()