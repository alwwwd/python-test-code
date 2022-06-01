def longest_words(file_name):
    with open(file_name, encoding='utf-8') as file:
        words = file.readline()
        max_length = 0

        list_of_words = []
        while words != "":
            words = words.replace("\n", "")

            if " " in words:
                words = words.split(" ")
            else:
                words = words.split() 

            for word in words:
                current_word_length = len(word)
                if current_word_length > max_length:
                    list_of_words.clear()
                    list_of_words.append(word)
                    max_length = current_word_length
                elif max_length == current_word_length:
                    list_of_words.append(word)

            words = file.readline()

    return list_of_words


 
print(longest_words("/Users/alex/Desktop/test-python/домашка_5/article.txt"))

