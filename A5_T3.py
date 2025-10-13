def askName():
    Name = input("Insert name: ")
    return Name

def greetUser(PName):
    print(f"Hello {PName}!")
    return None

def main():
    print("Program starting.")
    Name = askName()
    greetUser(Name)
    print("Program ending.")
    return None

main()