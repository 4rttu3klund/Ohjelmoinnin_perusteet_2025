print("Program starting.\n")

Start = int(input("Insert starting value: "))
Stop = int(input("Insert stopping value: "))

print("\nStarting while-loop:")
while True:
    if Start == Stop:
        print(Start, end='')
        break
    else:
        print(Start, end=' ')
    Start=Start+1
print("\n")
print("Program ending.")