def solution(box, n):
    box.sort()
    return (box[0]//n) * (box[1]//n) * (box[2]//n)