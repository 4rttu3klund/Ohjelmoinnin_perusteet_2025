LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def askRows():
    rows = []
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        rows.append(row)
    return "\n".join(rows)

def shiftCharacter(Character: str, Alphabets: str, Shift: int = 13) -> str:
    if Character in Alphabets:
        index = Alphabets.index(Character)
        return Alphabets[(index + Shift) % len(Alphabets)]
    return Character

def rot13(Content: str) -> str:
    result_chars = []
    for ch in Content:
        if ch in LOWER_ALPHABETS:
            result_chars.append(shiftCharacter(ch, LOWER_ALPHABETS))
        elif ch in UPPER_ALPHABETS:
            result_chars.append(shiftCharacter(ch, UPPER_ALPHABETS))
        else:
            result_chars.append(ch)
    return "".join(result_chars)

def writeFile(Filename: str, Content: str) -> None:
    File = open(Filename, "w", encoding="UTF-8")
    File.write(Content)
    return None

def main():
    print("Program starting.\n")
    print("Collecting plain text rows for ciphering.")
    plain = askRows()
    cipher = rot13(plain)
    print()
    print("#### Ciphered text ####")
    if cipher == "":
        print()
    else:
        for line in cipher.split("\n"):
            print(line)
    print()
    print("#### Ciphered text ####")
    FileName = input("Insert filename to save: ")
    if FileName.strip() == "":
        print("File name not defined.\nAborting save operation.")
    else:
        writeFile(FileName, cipher + ("\n" if cipher and not cipher.endswith("\n") else ""))
        print("Ciphered text saved!")
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()