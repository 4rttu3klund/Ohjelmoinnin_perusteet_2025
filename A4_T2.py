print("Program starting.\n")

Start = int(input("Insert starting value: "))
Stop = int(input("Insert stopping value: "))

print("\nStarting for-loop:")
for i in range(Start, Stop + 1):
    if i < Stop:
        print(i, end=' ')
    else:
        print(i, end='')
print("\n")
print("Program ending.")