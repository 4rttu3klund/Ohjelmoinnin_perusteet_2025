print("Program starting.")

print("\nOptions:\n1 - Celsius to Fahrenheit\n2 - Fahrenheit to Celsius\n0 - Exit")
Choice = int(input("Your choice: "))
if Choice == 1:
    Celsius = float(input("Insert the amount of Celsius: "))
    Fahrenheit = (Celsius * 1.8) + 32
    print(round(Celsius, 1), "°C equals to ", round(Fahrenheit, 1), "°F")
elif Choice == 2:
    Fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    Celsius = (Fahrenheit - 32) / 1.8
    print(round(Fahrenheit, 1), "°F equals to ", round(Celsius, 1), "°C")
elif Choice == 0:
    print("Exiting...")

print("\nProgram ending.")