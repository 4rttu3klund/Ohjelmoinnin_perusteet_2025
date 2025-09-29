print("Program starting.")
print("Insert two integers.")
Integer1 = int(input("Insert first integer: "))
Integer2 = int(input("Insert second integer: "))
print("Comparing inserted integers.")
if Integer1 > Integer2:
    print("First integer is greater.")
elif Integer1 < Integer2:
    print("Second integer is greater.")
else:
    print("Integers are the same.")

print("\nAdding integers together.")
Sum = Integer1 + Integer2
print(Integer1, "+", Integer2, "=", Sum)

print("\nChecking the parity of the sum...")
if Sum % 2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")
print("Program ending.")