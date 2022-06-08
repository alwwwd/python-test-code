import random as rand

# generate random numbers in list 
def generate_list_of_integers_in_range(min_value,max_value,number_of_values):
    list_of_values = []
    for i in range(0,number_of_values):
        list_of_values.append(rand.randint(min_value,max_value))

    return list_of_values

# sum lists function 
def sum_lists(summand_list_1, summand_list_2):
    result_list = []
    if len(summand_list_1) > len(summand_list_2):
        operations_number = len(summand_list_2)
    elif len(summand_list_1) < len(summand_list_2):
        operations_number = len(summand_list_1)
    else:
        operations_number = len(summand_list_1)

    for i in range(0,operations_number):
        result_list.append(summand_list_1[i]+summand_list_2[i])

    return result_list

# arithmetic mean function
def arithmetic_mean(list):
    sum = 0
    for i in range(0,len(list)):
        sum += list[i]
    
    return sum/len(list)


def max_number(list):
   Max = 0
   for item in list:
       if item > Max:
           Max = item
   return Max

def min_number(list):
    Min = list[0]
    for i in list[0:]:
        if i < Min:
            Min = i
    return Min

list_1 = generate_list_of_integers_in_range(10, 31, 10)
list_2 = generate_list_of_integers_in_range(10, 31, 11)
list_3 = sum_lists(list_1,list_2)
print(list_1)
print(list_2)
print(list_3)
print(arithmetic_mean(list_3))
maximum_number =  max_number(list_3)
print(maximum_number)
minimum_number = min_number(list_3)
print(minimum_number)