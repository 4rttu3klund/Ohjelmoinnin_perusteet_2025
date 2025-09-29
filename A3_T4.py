print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
Name = input("Before the menu, please insert your name: ")

print("\nOptions:\n1 - Print welcome message\n2 - Print the name backwards\n3 - Print the first character\n4 - Show the amount of characters in the name\n0 - Exit")
Choice = int(input("Your choice: "))
if Choice == 1:
    print("Welcome ", Name, "!", sep='')
elif Choice == 0:
    print("Exiting...")
elif Choice == 2:
    print("Your name backwards is \"", Name[::-1], "\"", sep='')
elif Choice == 3:
    print("The first character in name \"", Name, "\" is \"", Name[0], "\"", sep='')
elif Choice == 4:
    print("There are ", len(Name), " characters in the name \"", Name, "\"", sep='')
else:
    print("Unknown option.")

print("\nProgram ending.")