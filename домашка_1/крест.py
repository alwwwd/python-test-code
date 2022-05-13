for i in range(10 + 1):
    for j in range(10 + 1):
        if i == j:
            print('^', end = ' ')
        elif i == - j + 10:
            print('^', end = ' ')
        else:
            print(' ', end = ' ')
    print()