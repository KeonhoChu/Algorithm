#def solution(array, n):
#    result = []
#    array.sort()
#    for num in array:
#        intersect = abs(num - n)
#        result.append(intersect)
#    answer = array[result.index(min(result))]
#    return answer


def solution(array, n):
    array.sort()
    closest =array[0] 
    for num in array:
        if abs(num - n) < abs(closest - n):
            closest = num 
    return closest
