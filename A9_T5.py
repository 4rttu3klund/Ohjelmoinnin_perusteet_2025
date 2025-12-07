########################################################
# Task A9_T5
# Developer Arttu Eklund
# Date 2025-12-02
########################################################

def askIntByte(PPrompt: str) -> int:
    Feed = input(PPrompt)
    try:
        f = float(Feed)
        i = int(f)
    except ValueError:
        raise ValueError(f"\"{Feed}\" is non-numeric value.")
    if f != i:
        raise ValueError(f"\"{Feed}\" is non-numeric value.")
    if not (0 <= i <= 255):
        raise Exception(f"Value \"{i}\" is out of the range 0-255.")
    return i

def createHex(PRed: int, PGreen: int, PBlue: int) -> str:
    return "#{:02x}{:02x}{:02x}".format(PRed, PGreen, PBlue)

def main():
    print("Program starting.")
    try:
        r = askIntByte("Insert red: ")
        g = askIntByte("Insert green: ")
        b = askIntByte("Insert blue: ")
        hexValue = createHex(r, g, b)
        print("RGB Details:")
        print(f"- Red {r}")
        print(f"- Green {g}")
        print(f"- Blue {b}")
        print(f"- Hex {hexValue}")
    except Exception as e:
        print(e)
        print("Couldn't perform the designed task due to the invalid input values.")
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()