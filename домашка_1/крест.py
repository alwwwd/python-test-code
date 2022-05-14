for i in range(10):
    for j in range(10):
        if i == j:
            print('*', end = ' ')
        elif i == - j + 9:
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print()