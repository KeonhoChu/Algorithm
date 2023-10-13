def solution(array, height):
    count = 0
    for x in array:
        if x > height:
            count += 1
    return count