sp = "   "
st = "*"
def add_spase(sp,i):

    for i in range(1,6):
        if i ==  1:
            print(f"{sp}{st}")
        
        else:
            print(sp * i, st * i)
