########################################################
# Task A9_T2
# Developer Arttu Eklund
# Date 2025-12-02
########################################################

import sys

def main():
    print("Program starting.")
    user_input = input("Insert exit code(0-255): ")
    try:
        code = int(user_input)
    except ValueError:
        print("Error! '{}' is not a valid integer exit code.".format(user_input))
        sys.exit(1)
    if code == 0:
        print("Clean exit")
        sys.exit(0)
    else:
        print("Error code")
        sys.exit(1)
    return None

if __name__ == "__main__":
    main()