def solution(my_string):
    nums = ''
    total = 0
    for c in my_string:
        if c.isdigit():
            nums += c
        else:
            if nums:
                total += int(nums)
                nums = ''
    if nums:
        total += int(nums)
    return total