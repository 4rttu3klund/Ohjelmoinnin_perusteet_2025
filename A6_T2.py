def writeFile():
    FirstName = input("Insert first name: ")
    LastName = input("Insert last name: ")
    FileName = input("Insert filename: ")
    file = open(FileName, "w", encoding="UTF-8")
    file.write(FirstName + '\n')
    file.write(LastName + '\n')
    file.close()
    return None

def main():
    print("Program starting.")
    writeFile()
    print("Program ending.")

if __name__ == "__main__":
    main()