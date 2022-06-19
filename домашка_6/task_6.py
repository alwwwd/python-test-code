def is_palindrom_word(input_word : str) -> bool: 
    for i in range(len(input_word)//2):
        j = i + 1
        if input_word[i] != input_word[-j]:
            return False

    return True

if is_palindrom_word(input("введите строку:")):
    print("yes")
else: 
    print("no")
