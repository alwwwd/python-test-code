import random as rand
rand_numbers_1 = []
rand_numbers_2 = []
rand_numbers_3 = []

# generate random numbers in list 
def rand_numbers(
    rand_numbers_1,
    rand_numbers_2):
    for i in range(0,10):
        gen_number1 = rand.randint(10,31)
        rand_numbers_1.append(gen_number1)

        gen_number2 = rand.randint(10,31)
        rand_numbers_2.append(gen_number2)
    return f"первый список ({rand_numbers_1}),\nвторой список ({rand_numbers_2})," 

# sum lists function 
def sum_lists(
    rand_numbers_1,
    rand_numbers_2,
    rand_numbers_3):
        for i in range(0,10):
            rand_numbers_3.append(
                rand_numbers_1[i]+rand_numbers_2[i]
            )
        return f"несортированый третий список ({rand_numbers_3}),"

# arithmetic meanfunction
def arithmetic_mean(
    rand_numbers_3=rand_numbers_3):
    for i in range(1,10):
        a = rand_numbers_3[i-1]+ rand_numbers_3[i]
        a =int(a/len(rand_numbers_3))
    return f"среднее арефмитическое третего списка ({a})"

# sort lists
    
  
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
    return f"cортированый третий список({arr}),"




print(
    rand_numbers(
        rand_numbers_1,
        rand_numbers_2)
        )

print(
    sum_lists(
        rand_numbers_1,
        rand_numbers_2,
        rand_numbers_3)
        )

print(
    sort(
    rand_numbers_3, 
    "less")
    )
print(
    arithmetic_mean()
    )
print(max(rand_numbers_3))