def sorter (number, items_in_list):
    for i in range(items_in_list):
        sort_list = number        
        for j in range(items_in_list):
            if sort_list[j] > sort_list[j+1]:
                sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]
                print(sort_list)

    return print(sort_list)