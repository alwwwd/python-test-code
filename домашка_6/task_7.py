def chess_board(size : int):
    for i in range(size):

        for j in range(size):
            if (i + j) % 2 == 0:
                print("#",end="")
            else:
                print("%",end="")
        print("")
#  012345            
# 0#%#%#%
# 1%#%#%#
# 2#%#%#%
# 3%#%#%#
# 4#%#%#%
# 5%#%#%#


# i j R
# ч ч #
# ч н *
# н ч *
# н н #
chess_board(10)