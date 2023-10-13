def solution(numbers):
    word_dict = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    answer = ""
    temp = ""
    for i in numbers:
        temp += i
        if temp in word_dict:
            answer += str(word_dict[temp])
            temp = ""
    return int(answer)