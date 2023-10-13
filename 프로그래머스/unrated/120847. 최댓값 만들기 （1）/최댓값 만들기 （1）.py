def solution(numbers):
    num1 = 0
    num2 = 0
    answer = 0

    numbers.sort()

    num1 = numbers.pop()
    num2 = numbers.pop()
    answer = num1 * num2

    return answer