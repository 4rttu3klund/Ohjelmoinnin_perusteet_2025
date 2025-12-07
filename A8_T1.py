import time

def main():
    pauseDuration = None
    print("Program starting.")
    while True:
        print("Options:")
        print("1 - Set pause duration")
        print("2 - Activate pause")
        print("0 - Exit")
        choice = input("Your choice: ")
        if choice == "1":
            try:
                value = float(input("Insert pause duration (s): "))
                pauseDuration = value
            except ValueError:
                print("Invalid duration!")
            print()
        elif choice == "2":
            if pauseDuration is None:
                print("Pause is not set.")
                print("Set pause first.\n")
            else:
                print(f"Pausing for {pauseDuration} seconds.")
                time.sleep(pauseDuration)
                print("Unpaused.\n")
        elif choice == "0":
            print("Exiting program.\n")
            break
        else:
            print("Unknown option!\n")
    print("Program ending.")

if __name__ == "__main__":
    main()