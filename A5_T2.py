def frameWord(PWord):
    print("*" * (len(PWord) + 4))
    print("*", PWord, "*")
    print("*" * (len(PWord) + 4))
    return None

def main():
    print("Program starting.")
    Word = input("Insert word: ")
    print()
    frameWord(Word)
    print()
    print("Program ending.")
    return None

main()