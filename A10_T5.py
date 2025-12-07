########################################################
# Task A10_T5
# Developer Arttu Eklund
# Date 2025-12-05
########################################################

import sys

def recursiveFactorial(PNum: int) -> int:
    if PNum <= 1:
        return 1
    return PNum * recursiveFactorial(PNum - 1)

def buildFactorString(n: int) -> str:
    return "*".join(str(i) for i in range(1, n + 1))

def main() -> None:
    print("Program starting.")
    try:
        num = int(input("Insert factorial: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        sys.exit(1)
    if num < 1:
        print("Error: Factorial must be larger than 0.")
        sys.exit(1)
    print(f"Factorial {num}!")
    factString = buildFactorString(num)
    result = recursiveFactorial(num)
    print(f"{factString} = {result}")
    print("Program ending.")

if __name__ == "__main__":
    main()