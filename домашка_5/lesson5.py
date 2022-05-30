# Задание 1

# text = '''Жил-был в норе под землей хоббит. Не в какой-то там мерзкой грязной сырой норе, где со всех сторон торчат хвосты червей 
# и противно пахнет плесенью, но и не в сухой песчаной голой норе, где не на что сесть и нечего съесть. Нет, нора была хоббичья, а значит — 
# благоустроенная. Она начиналась идеально круглой, как иллюминатор, дверью, выкрашенной зеленой краской, с сияющей медной ручкой точно 
# посередине. Дверь отворялась внутрь, в длинный коридор, похожий на железнодорожный туннель, но туннель без гари и без дыма и тоже очень 
# благоустроенный: стены там были обшиты панелями, пол выложен плитками и устлан ковром, вдоль стен стояли полированные стулья, и всюду 
# были прибиты крючочки для шляп и пальто, так как хоббит любил гостей. Туннель вился все дальше и дальше и заходил довольно глубоко, но не 
# в самую глубину Холма, как его именовали жители на много миль в окружности. По обеим сторонам туннеля шли двери — много-много круглых 
# дверей. Хоббит не признавал восхождений по лестницам: спальни, ванные, погреба, кладовые (целая куча кладовых), гардеробные (хоббит отвел 
# несколько комнат под хранение одежды), кухни, столовые располагались в одном этаже и, более того, в одном и том же коридоре. Лучшие 
# комнаты находились по левую руку, и только в них имелись окна — глубоко сидящие круглые окошечки с видом на сад и на дальние луга, 
# спускавшиеся к реке.'''

# text = text.replace(".", "").replace(",", "").replace("(", "").replace(")", "").replace("-", "").replace(":", "").replace("\n", "").replace(" —", "")

# words = {}

# for word in text.split(" "):
#     if word in words:
#         words[word] += 1
#     else:
#         words[word] = 1

# words_list = words.items()

# words_list = sorted(words_list, key = lambda x: x[1], reverse = True)

# for key, value in words_list:
#     print(key + " : " + str(value))

# [(1, 2), (1, 3)]


# Пример реализации функции сортировки с уетом ключа сортировки
# def greater(a, b):
#     return a > b

# def less(a, b):
#     return a < b

# def doNothing(a):
#     return a

# def sort(arr, reverse = False, key = lambda x : x):
#     if reverse:
#         func = less
#     else:
#         func = greater

#     for i in range(len(arr)):
#         isSorted = True
#         for j in range(len(arr) - 1 - i):
#             if func(key(arr[j]), key(arr[j + 1])):
#                 temp = arr[j]
#                 arr[j] = arr[j + 1]
#                 arr[j + 1] = temp

#         if isSorted:
#             return

# a = [["a", 3], ["d", 1], ["c", 2]]

# sort(a, key = lambda x : x[1])

# print(a)

# file = open("test.txt", "a")

# file.write("adad")
# file.write(" xcbcb")
# words = ["dadad", "adada", "adad"]
# file.writelines(words)


# "r" - режим чтения. Если файл не существует
# программа завершается аварийно
# "w" - режим записи. Каждый раз создается новый файл
# "a" - режим добавления 


file = open("article.txt", "r")

# Считывание файла целиком и возврат строки
print(file.read())
# Считывание файла целиком и возврат массива строк
for word in file.readlines():
    print(word, end = "")


# Считыванеи файла по строкам
# string = None

# while string != "":
#     string = file.readline()

#     print(string)

print(file.tell())
print(file.read(4))
print(file.seek(0))
print(file.read(4))

# УСТРОЙСТВО ТЕКСТОВОГО ФАЙЛА
# 1. Каждая строка кроме последней заканчивается символом z
# 2. Каждый файл заканчивается маркером конца файла EOF или 0
# 3. При считывании данных с файла создается файловый указатель, который
# помечает следующий символ, который будет считан первым при
# последующей операции чтения

# Функции работы с файловым указателем
# file.tell() - возвращает индекс символа, который будет считан первым при 
# операции чтения
# file.seek() - устанавливает позицию файлового указателя
