def copyFile():
    Source = input("Insert source filename: ")
    Destination = input("Insert destination filename: ")
    print(f"Reading file '{Source}' content.")
    print("File content ready in memory.")
    print(f"Writing content into file '{Destination}'.")
    print("Copying operation complete.")
    SFile = open(Source, 'r', encoding="UTF-8")
    DFile = open(Destination, 'w', encoding="UTF-8")
    while True:
        line = SFile.readline()
        DFile.write(line)
        if len(line) == 0:
            break
    SFile.close()
    DFile.close()
    return None

def main():
    print("Program starting.")
    print("This program can copy a file.")
    copyFile()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()