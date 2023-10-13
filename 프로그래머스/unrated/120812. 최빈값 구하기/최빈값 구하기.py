def solution(array):
    counter = {}
    for num in array:
        if num not in counter:
            counter[num] = 1
        else:
            counter[num] += 1
    max_count = 0
    max_num = -1
    for num, count in counter.items():
        if count > max_count:
            max_count = count
            max_num = num
        elif count == max_count:
            max_num = -1
    
    return max_num