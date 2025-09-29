print("Program starting.")

print("\nOptions:\n1 - Celsius to Fahrenheit\n2 - Fahrenheit to Celsius\n0 - Exit")
Choice = int(input("Your choice: "))
if Choice == 1:
    Celsius = round(float(input("Insert the amount of Celsius: ")), 1)
    Fahrenheit = round((Celsius * 1.8) + 32, 1)
    print(Celsius, "°C equals to ", Fahrenheit, "°F")
elif Choice == 2:
    Fahrenheit = round(float(input("Insert the amount of Fahrenheit: ")), 1)
    Celsius = round((Fahrenheit - 32) / 1.8, 1)
    print(Fahrenheit, "°F equals to ", Celsius, "°C")
elif Choice == 0:
    print("Exiting...")

print("\nProgram ending.")