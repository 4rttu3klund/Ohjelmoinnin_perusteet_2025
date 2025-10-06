print("Program starting.\n")

Start = int(input("Insert starting point: "))
Stop = int(input("Insert stopping point: "))
Inspect = int(input("Insert inspection point: "))
rule_broken = False

print()

if Start >= Stop:
    print("Starting point value must be less than the stopping point value.")
    rule_broken = True

if Inspect < Start or Inspect > Stop:
    print("Inspection value must be within the range of start and stop.")
    rule_broken = True

if not rule_broken:
    print("First loop - inspection with break:")
    for i in range(Start, Stop):
        if i == Inspect:
            break
        elif i < Inspect - 1:
            print(i, end=' ')
        else:
            print(i, end='')
    print("\nSecond loop - inspection with continue:")
    for i in range(Start, Stop):
        if i == Inspect:
            continue
        elif i < Stop - 1:
            print(i, end=' ')
        else:
            print(i, end='')
    print()
print()    
print("Program ending.")