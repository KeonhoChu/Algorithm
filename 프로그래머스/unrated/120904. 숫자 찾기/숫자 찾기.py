def solution(num, k):
    str_num = str(num)
    if str(k) in str_num:
        return str_num.index(str(k))+1
    else:
        return -1