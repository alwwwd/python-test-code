
 
def longest_words(file, lines_of_file):   
    for i in  range(lines_of_file):
        print(file.read())
        if file != " ":     
            string = file.read(i)
            print(string)
        else:
            pass




file = open("/Users/alex/Desktop/test-python/домашка_5/article.txt", "r")


longest_words(file,9)



