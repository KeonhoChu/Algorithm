def solution(name, yearning, photo):
    # 이름과 그리움 점수를 매핑하는 딕셔너리 생성
    name_to_score = {n: y for n, y in zip(name, yearning)}

    result = []  # 각 사진별 추억 점수를 저장할 리스트

    for pic in photo:
        score = 0
        for person in pic:
            if person in name_to_score:
                score += name_to_score[person]

        result.append(score)

    return result