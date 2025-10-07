print("Program starting.")

Integer = int(input("Insert a positive integer: "))
Step = 0
List = [str(Integer)]

while Integer != 1:
    if Integer % 2 == 0:
        Integer = Integer // 2
    else:
        Integer = Integer * 3 + 1
    List.append(str(Integer))
    Step += 1

print(' -> '.join(List))
print("Sequence had", Step, "total steps.\n")

print("Program ending.")