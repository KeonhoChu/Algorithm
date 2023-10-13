def solution(my_string):
    numbers = [int(c) for c in my_string if c.isdigit()]
    numbers.sort()
    return numbers
