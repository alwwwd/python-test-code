def sum_lists(
    rand_numbers_1,
    rand_numbers_2,
    rand_numbers_3, 
    range_max = 10):
    for i in range(0,range_max):
        rand_numbers_3.append(
            rand_numbers_1[i]+rand_numbers_2[i]
        )
    return f"несортированый{rand_numbers_3}"
