from A8_T2_lib import add, subtract, multiply, divide

def showOptions() -> None:
    print("Options:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")
    return None

def askChoice() -> int:
    choice = input("Your choice: ")
    if choice.isdigit():
        return int(choice)
    return -1

def askValue(PPrompt: str) -> float:
    return float(input(PPrompt))

def main() -> None:
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()
        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice == 1:
            a = askValue("Insert first addend value: ")
            b = askValue("Insert second addend value: ")
            result = add(a, b)
            print(f"{a} + {b} = {result}\n")
        elif choice == 2:
            a = askValue("Insert minuend value: ")
            b = askValue("Insert subtrahend value: ")
            result = subtract(a, b)
            print(f"{a} - {b} = {result}\n")
        elif choice == 3:
            a = askValue("Insert multiplicand value: ")
            b = askValue("Insert multiplier value: ")
            result = multiply(a, b)
            print(f"{a} * {b} = {result}\n")
        elif choice == 4:
            a = askValue("Insert dividend value: ")
            b = askValue("Insert divisor value: ")
            if b == 0:
                print("Division by zero error!\n")
            else:
                result = divide(a, b)
                print(f"{a} / {b} = {result}\n")
        else:
            print("Unknown option!\n")
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()