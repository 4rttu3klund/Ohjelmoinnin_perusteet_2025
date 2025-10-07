print("Program starting.\n")

print("Check multiplicative persistence.")
Integer = input("Insert an integer: ")
Step = 0

while len(Integer) > 1:
    Digits = [int(d) for d in Integer]
    Line = ' * '.join(Integer) + ' = '
    Product = 1
    for d in Digits:
        Product = Product * d
    print(f"{Line}{Product}")
    Integer = str(Product)
    Step = Step + 1

print("No more steps.\n")
print(f"This program took {Step} step(s)\n")
print("Program ending.")