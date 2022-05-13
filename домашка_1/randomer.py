import random

randomer = random.randint(1, 100)
print(randomer)
res = [int(input("Какое чиcло я загадал"))]
print(res[:1])
while 1 == 1:
    if randomer ==  res:
        print('ты угадал')
    else:
        print("неверно")
        res.append(int(input("Какое чиcло я загадал")))
        print(res)
