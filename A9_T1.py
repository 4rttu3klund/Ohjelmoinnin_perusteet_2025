########################################################
# Task A9_T1
# Developer Arttu Eklund
# Date 2025-12-02
########################################################

def main():
    print("Program starting.\n")
    total = 0.0
    while True:
        user_input = input("Insert a floating-point value (0 to stop): ")
        try:
            value = float(user_input)
            if value == 0:
                break
            total += value
        except ValueError:
            print("Error! '{}' couldn't be converted to float.".format(user_input))
    print("\nFinal sum is {:.2f}".format(total))
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()