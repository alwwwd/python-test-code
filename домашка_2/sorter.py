#import random
list = [11,12 ,8,9,5]

def sorter (number):
    sort_list = number
    items_in_list = len(sort_list)
    for i in range(items_in_list):
        movin_flag = True
        for j in range(0, items_in_list - 1 - i):
            if sort_list[j] > sort_list[j+1]:
                sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]
                movin_flag = False
                print(sort_list)

        if movin_flag == False:
	        break


    return print(sort_list)


sorter(list)
