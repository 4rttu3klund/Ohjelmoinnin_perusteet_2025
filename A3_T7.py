print("Program starting.")

print("Testing decision structures.")
Integer = int(input("Insert an integer: "))
print("Options:\n1 - In one multi-branched decision\n2 - In multiple independent if-statements\n0 - Exit")
Choice = int(input("Your choice: "))

if Choice == 1:
    print("Using one multi-branched decision structure.")
    if Integer >= 400:
        Integer += 44
        print("Result is", Integer)
    elif Integer >= 200:
        Integer += 22
        print("Result is", Integer)
    elif Integer >= 100:
        Integer += 11
        print("Result is", Integer)
    else:
        print("Result is", Integer)
elif Choice == 2:
    print("Using multiple independent if-statements structure.")
    if Integer >= 400:
        Integer += 44
    if Integer >= 200:
        Integer += 22
    if Integer >= 100:
        Integer += 11
    else:
        print("Result is", Integer)
    print("Result is", Integer)
elif Choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")