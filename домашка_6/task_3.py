a = input()
 
digits = "02468"
 
even = 0
odd = 0
 
for i in a:
    if i in digits:
        even += 1
    else:
        odd += 1
 
print("Even: %d" % (even, odd))