import random as rand

def rand_number(
    rand_numbers_1,
    rand_numbers_2,
    range_max = 10):
    for i in range(0,range_max):
        gen_number1 = rand.randint(10,31)
        rand_numbers_1.append(gen_number1)

        gen_number2 = rand.randint(10,31)
        rand_numbers_2.append(gen_number2)
    return f"первый список({rand_numbers_1}),\nвторой список({rand_numbers_2})" 

