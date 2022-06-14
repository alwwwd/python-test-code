def draw_pyramide(size : int):
    for i in range(size):
        print(" " * (size - i - 1),end="")
        for j in range(i+1):
            print("*",end=" ")
        print("")

draw_pyramide(15)