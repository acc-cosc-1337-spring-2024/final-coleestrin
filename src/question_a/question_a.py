def sum_list(list: list) -> int:
    sum = 0
    
    for num in list:
        sum += num
    
    return sum

def average_of_list(list: list) -> int:
    return sum_list(list) / len(list)