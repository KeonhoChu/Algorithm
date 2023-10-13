def solution(money):
    price = 5500
    count = money // price
    remain = money % price
    return [count, remain]