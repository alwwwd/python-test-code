def palindrom_word(input_word):
    for i in range(len(input_word)):
        j = i + 1
        if input_word[i] == input_word[-j]:
            print("yes")
            break
        else:
            print("no")
            break
palindrom_word(str(input("введи палиндром:")))