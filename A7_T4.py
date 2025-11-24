DELIMITER = ";"

class TIMESTAMP:
    def __init__(self):
        self.weekday = ""
        self.hour = ""
        self.consumption = 0.0
        self.price = 0.0

def readTimestamps(Filename: str) -> list[TIMESTAMP]:
    print(f'Reading file "{Filename}".')
    Timestamps: list[TIMESTAMP] = []
    File = open(Filename, "r", encoding="UTF-8")
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
        ts.hour = (f"{columns[1]}:00")
        ts.consumption = float(columns[2])
        ts.price = float(columns[3])
        Timestamps.append(ts)
        columns.clear()
    return Timestamps

def displayTimestamps(Timestamps: list[TIMESTAMP]):
    print("Electricity usage:")
    for ts in Timestamps:
        total = ts.consumption * ts.price
        print(
            f" - {ts.weekday} {ts.hour}, price {ts.price:.2f}, "
            f"consumption {ts.consumption:.2f} kWh, total {total:.2f} €"
        )
    return None

def main():
    print("Program starting.")
    Filename = input("Insert filename: ")
    Timestamps = readTimestamps(Filename)
    if not Timestamps:
        print("No valid data found.")
        print("Program ending.")
        return
    displayTimestamps(Timestamps)
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()