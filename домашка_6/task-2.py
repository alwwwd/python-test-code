from pickletools import read_unicodestringnl
import random as rand

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

def sum_list(
    rand_numbers_1,
    rand_numbers_2,
    rand_numbers_3, 
    range_max = 10):
    for i in range(0,range_max):
        rand_numbers_3.append(
            rand_numbers_1[i]+rand_numbers_2[i]
        )
        


rand_number(
    rand_numbers_1,
    rand_numbers_2)
sum_list(
    rand_numbers_1,
    rand_numbers_2,
    rand_numbers_3)
print(rand_numbers_1)
#print(max(rand_numbers_1))
print(rand_numbers_2)
print(rand_numbers_3)