def solution(n, k):
    # 양꼬치 요금 계산
    total_price = n * 12000
    
    # 음료수 요금 계산
    drink_count = k - (n // 10)
    total_price += drink_count * 2000
    
    return total_price