def fibo_numbers(number_of_values):
    if number_of_values <= 0:
        return []
        
    fibo_elements = []
    current = 1
    previous = 0
    fibo_elements.append(current)

    for i in range(0,number_of_values-1):
        fibo_elements.append(current+previous)
        previous = current
        current = fibo_elements[-1]
      
    return fibo_elements

fibo = fibo_numbers(1)
print(fibo)
