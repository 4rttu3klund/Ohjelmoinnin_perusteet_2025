print("Program starting.")
print("Welcome to the unit converter program!\nFollow the menu instructions below.")

print("\nOptions:\n1 - Length\n2 - Weight\n0 - Exit")
MainChoice = float(input("Your choice: "))

if MainChoice == 1:
    print("\nLength options:\n1 - Meters to kilometers\n2 - Kilometers to meters\n0 - Exit")
    LengthChoice = float(input("Your choice: "))
    if LengthChoice == 1:
        Meters = float(input("Insert meters: "))
        Kilometers = Meters / 1000
        print(round(Meters, 1), "m is", round(Kilometers, 1), "km")
    elif LengthChoice == 2:
        Kilometers = float(input("Insert kilometers: "))
        Meters = Kilometers * 1000
        print(round(Kilometers, 1), "km is", round(Meters, 1), "m")
    elif LengthChoice == 0:
        print("Exiting...")
    else:
        print("Unknown option.")
elif MainChoice == 2:
    print("\nWeight options:\n1 - Grams to pounds\n2 - Pounds to grams\n0 - Exit")
    WeightChoice = float(input("Your choice: "))
    if WeightChoice == 1:
        Grams = float(input("Insert grams: "))
        Pounds = Grams * 0.002205
        print(round(Grams, 1), "g is", round(Pounds, 1), "lb")
    elif WeightChoice == 2:
        Pounds = float(input("Insert pounds: "))
        Grams = Pounds * 453.6
        print(round(Pounds, 1), "lb is", round(Grams, 1), "g")
    elif WeightChoice == 0:
        print("Exiting...")
    else:
        print("Unknown option.")
elif MainChoice == 0:
    print("\nExiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")