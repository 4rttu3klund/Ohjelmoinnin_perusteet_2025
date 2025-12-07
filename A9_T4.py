########################################################
# Task A9_T4
# Developer Arttu Eklund
# Date 2025-12-02
########################################################

TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius():
    feed = input("Insert Celsius: ")
    try:
        C = float(feed)
    except ValueError:
        raise ValueError(f"could not convert string to float: '{feed}'")
    if C < TEMP_MIN or C > TEMP_MAX:
        raise Exception(f"{C} temperature out of range.")
    return C

def main():
    print("Program starting.")
    try:
        C = collectCelsius()
        print(f"You inserted {C} °C")
    except Exception as e:
        print(e)
    print("Program ending.")

if __name__ == "__main__":
    main()