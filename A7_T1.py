def CollectInt():
    Numbers: list[int] = []
    while True:
        Integer = int(input("Insert positive integer (negative stops): "))
        if Integer <= 0:
            break
        else:
            Numbers.append(Integer)
    print("Stopped collecting positive integers.")
    return Numbers

def DisplayInt(Numbers):
    if len(Numbers) == 0:
        print("No integers to display.")
    else:
        print(f"Displaying {len(Numbers)} integers:")
        for Index, Value in enumerate(Numbers):
            Ordinal = Index + 1
            print(f"- Index {Index} => Ordinal {Ordinal} => Integer {Value}")
    return None

def main():
    print("Program starting.")
    print("Collect positive integers.")
    Numbers = CollectInt()
    DisplayInt(Numbers)
    print("Program ending.")

if __name__ == "__main__":
    main()