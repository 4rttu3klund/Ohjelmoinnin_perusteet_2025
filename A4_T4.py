print("Program starting.\n")
Feed = "x"
Word = -1
Character = 0
while True:
    if len(Feed)==0:
        break
    else:
        Feed = input("Insert word (empty stops): ")
    Character = Character + len(Feed)
    Word = Word + 1
print("\nYou inserted:\n-", Word, "words\n-", Character, "characters")
print("\nProgram ending.")