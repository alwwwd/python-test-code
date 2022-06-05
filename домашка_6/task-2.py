import random as rand
from sorter import sort


rand_numbers_1 = []
rand_numbers_2 = []
rand_numbers_3 = []
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
 
def sum_list(
    rand_numbers_1,
    rand_numbers_2,
    rand_numbers_3, 
    range_max = 10):
    for i in range(0,range_max):
        rand_numbers_3.append(
            rand_numbers_1[i]+rand_numbers_2[i]
        )
    return f"несортированый{rand_numbers_3}"
     

def third(rand_numbers_3= rand_numbers_3,range_max = 10):
    a = None
    for i in range(10):
        a = rand_numbers_3[i] + rand_numbers_3[i+1]
        print(a)


print(rand_number(
        rand_numbers_1,
        rand_numbers_2))
#print(max(rand_numbers_1))
print(sum_list(
    rand_numbers_1,
    rand_numbers_2,
    rand_numbers_3))

print(sort(rand_numbers_3, "greater"))
print(third())