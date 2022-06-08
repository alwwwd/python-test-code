def number_is_digits(a):
    digits = "02468" 
    even = 0
    odd = 0
    for i in a:
        if i in digits:
            even += 1
        else:
            odd += 1
    return even

how_many_even_numbers = number_is_digits(input("введите числа:"))
print(f"{how_many_even_numbers} чётных числа")