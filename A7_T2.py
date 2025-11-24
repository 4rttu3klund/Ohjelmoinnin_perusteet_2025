def inputIntegers() -> list[int]:
    userInput = input("Insert comma separated integers: ")
    Values = [v.strip() for v in userInput.split(",")]

    validIntegers = []
    for v in Values:
        if v.lstrip('-').isdigit():
            validIntegers.append(int(v))
        elif v:
            print(f"Invalid value '{v}' detected.")
    return validIntegers

def analyseIntegers(numbers: list[int]):
    if not numbers:
        print("No valid integers to analyze.")
        return
    total = sum(numbers)
    parity = "even" if total % 2 == 0 else "odd"
    print(f"There are {len(numbers)} integers in the list.")
    print(f"Sum of the integers is {total} and it's {parity}")
    return None

def main():
    print("Program starting.")
    Numbers = inputIntegers()
    analyseIntegers(Numbers)
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()