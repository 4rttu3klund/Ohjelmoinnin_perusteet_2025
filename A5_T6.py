def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None

def askChoice():
    choice = input("Your choice: ")
    if not choice.isnumeric():
        print("Unknown option!")
        return -1
    return int(choice)

def main():
    print("Program starting.")
    count = 0
    while True:
        showOptions()
        choice = askChoice()
        if choice == 1:
            print(f"Current count - {count}\n")
        elif choice == 2:
            count += 1
            print("Count increased!")
        elif choice == 3:
            count = 0
            print("Cleared count!")
        elif choice == 0:
            print("Exiting program.\n")
            break
        elif choice == -1:
            print()
        else:
            print("Unknown option!\n")
    print("Program ending.")
    return None

main()