cycle = 10 # переменная для цикла
square = cycle - 1
for i in range(cycle):
    for j in range(cycle):
        if i == 0 or i == square or j == 0 or j == square:
            print("#", end = "")
        else:
            print("#", end= "")
    print("")