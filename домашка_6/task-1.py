fibo = []
def fibo_numbers(first):
    fibo.append(first)
    fibo.append(first)
    for i in range(0,10):
        fibo.append(fibo[i]+ fibo[i+1])

fibo_numbers(2)
print(fibo)