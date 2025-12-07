########################################################
# Task A9_T3
# Developer Arttu Eklund
# Date 2025-12-02
########################################################

import sys

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    try:
        with open(filename, "r", encoding="UTF-8") as f:
            content = f.read()
    except Exception:
        print(f"Couldn't read file \"{filename}\".")
        sys.exit(1)
    print(f"## {filename} ##")
    print(content, end="")
    print(f"## {filename} ##")
    print("Program ending.")

if __name__ == "__main__":
    main()