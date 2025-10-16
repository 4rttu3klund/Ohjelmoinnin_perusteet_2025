def insertWord() -> str:
    return input("Insert word: ")

def showWord(PWord: str):
    print(f'Current word - "{PWord}"\n')
    return None

def reverseWord(PWord: str):
    print(f'Word reversed - "{PWord[::-1]}"\n')
    return None

def menu():
    print("Options:")
    print("1 - Insert word")
    print("2 - Show current word")
    print("3 - Show current word in reverse")
    print("0 - Exit")
    return input("Your choice: ")

def main():
    print("Program starting.")
    Word = ""
    while True:
        choice = menu()
        if choice == "1":
            Word = insertWord()
            print()
        elif choice == "2":
            showWord(Word)
        elif choice == "3":
            reverseWord(Word)
        elif choice == "0":
            print("Exiting program.\n")
            break
        else:
            print("Unknown option! Try again.\n")
    print("Program ending.")
    return None

main()