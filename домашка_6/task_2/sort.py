def greater(a, b):
    return a > b

def less(a, b):
    return a < b

def sort(arr, flag):
    if flag:
        func = greater
    else:
        func = less

    for i in range(len(arr)):
        moving_flag = True
        for j in range(len(arr) - 1 - i):
            if func(arr[j], arr[ j + 1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                moving_flag = False

        if moving_flag:
            break
    return arr