import svgwrite
from A8_T6_lib import drawSquare, drawCircle, saveSvg

def showMenu() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
    print("0 - Exit")

def main() -> None:
    print("Program starting.")
    Dwg = svgwrite.Drawing()
    while True:
        showMenu()
        choice = input("Your choice: ")
        if choice == "0":
            print("Exiting program.\n")
            break
        elif choice == "1":
            drawSquare(Dwg)
        elif choice == "2":
            drawCircle(Dwg)
        elif choice == "3":
            saveSvg(Dwg)
        else:
            print("Unknown option!\n")
    print("Program ending.")

if __name__ == "__main__":
    main()