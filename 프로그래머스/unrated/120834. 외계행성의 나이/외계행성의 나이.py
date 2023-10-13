def solution(age):
    str_age = str(age)
    answer = ''
    lst =["a","b","c","d","e","f","g","h","i","j"]
    for ch in str_age:
        for i in range(0,10):
            if int(ch) == i:
                answer += lst[i]
    return answer