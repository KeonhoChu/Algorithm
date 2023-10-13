def solution(sides):
    a, b, c = sorted(sides)
    if a + b > c:
        return 1
    else: return 2