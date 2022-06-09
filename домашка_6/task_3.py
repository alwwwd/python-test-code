# def number_is_digits(a):
#     digits = "02468" 
#     even = 0
#     number_as_str = str(a)
#     for i in number_as_str:
#         if i in digits:
#             even += 1

#     return even

# how_many_even_numbers = number_is_digits(int(input("введите числа:")))
# print(f"{how_many_even_numbers} чётных цифр")

def digits_of_even_digits(number):
    even_digits = 0
    while number > 0:
        first_digit = number % 10
        if  first_digit % 2 == 0:
            even_digits += 1
            number //= 10    

    return even_digits 


print(digits_of_even_digits(24688))
