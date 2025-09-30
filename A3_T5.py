print("Program starting.")

print("\nOptions:\n1 - Celsius to Fahrenheit\n2 - Fahrenheit to Celsius\n0 - Exit")
Choice = int(input("Your choice: "))
if Choice == 1:
    Celsius = float(input("Insert the amount of Celsius: "))
    Fahrenheit = (Celsius * 1.8) + 32
    print(f"{Celsius:.1f} °C equals to {Fahrenheit:.1f} °F")
elif Choice == 2:
    Fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    Celsius = (Fahrenheit - 32) / 1.8
    print(f"{Fahrenheit:.1f} °F equals to {Celsius:.1f} °C")
elif Choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")