########################################################
# Task A9_T6
# Developer Arttu Eklund
# Date 2025-12-02
########################################################

def showOptions() -> None:
    print("Options:")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")

def askChoice() -> int:
    try:
        return int(input("Your choice: "))
    except Exception:
        return -1

def saveLines(PLines: list[str]) -> None:
    if len(PLines) == 0:
        print("Nothing to save.")
        return
    try:
        filename = input("Insert filename: ")
        with open(filename, "w", encoding="UTF-8") as f:
            for line in PLines:
                f.write(line + "\n")
    except Exception:
        print("File error!")

def insertLine(PLines: list[str]) -> None:
    text = input("Insert text: ")
    PLines.append(text)
    
def onInterrupt(PLines: list[str]) -> None:
    if len(PLines) == 0:
        print("Closing suddenly.")
        print("Program ending.")
        raise SystemExit
    print("Keyboard interrupt and unsaved progress!")
    try:
        confirm = input("Save before quit(y/n)?: ")
        if confirm.lower() == "y":
            filename = input("Insert filename: ")
            try:
                with open(filename, "w", encoding="UTF-8") as f:
                    for line in PLines:
                        f.write(line + "\n")
            except Exception:
                print("File error.")
    except Exception:
        pass
    print("Program ending.")
    raise SystemExit

def main() -> None:
    Lines: list[str] = []
    Choice = -1
    print("Program starting.")
    try:
        while Choice != 0:
            showOptions()
            Choice = askChoice()
            if Choice == 1:
                insertLine(Lines)
            elif Choice == 2:
                saveLines(Lines)
            elif Choice == 0:
                print("Exiting program.")
            else:
                print("Unknown option!")
            print("")
    except KeyboardInterrupt:
        onInterrupt(Lines)
    Lines.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()