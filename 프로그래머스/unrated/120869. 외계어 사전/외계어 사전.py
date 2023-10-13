def solution(spell, dic):
    for word in dic:
        if  len(word) == len(spell) and set(spell) == set(word):
            return 1
    return 2