def solution(n):
    is_prime = [True] * (n+1) # 소수 판별을 위한 리스트 생성
    is_prime[0], is_prime[1] = False, False # 0, 1은 소수가 아님
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]: # i가 소수인 경우
            for j in range(i+i, n+1, i): # i의 배수는 모두 소수가 아님
                is_prime[j] = False
    
    cnt = 0
    for i in range(2, n+1):
        if not is_prime[i]: # i가 합성수인 경우
            divisors = 0
            for j in range(1, int(i**0.5)+1):
                if i % j == 0:
                    if i//j == j: # 제곱근인 경우
                        divisors += 1
                    else:
                        divisors += 2
            if divisors >= 3: # 약수의 개수가 3개 이상인 경우
                cnt += 1
    
    return cnt