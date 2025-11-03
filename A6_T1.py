def readFile(PFilename):
    print(f'#### START "{PFilename}" ####')
    file = open(PFilename, 'r', encoding="UTF-8")
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        print(line, end="")
    file.close()
    print(f'\n#### END "{PFilename}" ####')
    return None

def main():
    print("Program starting.")
    print("This program can read a file.")
    Filename = input("Insert filename: ")
    readFile(Filename)
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()