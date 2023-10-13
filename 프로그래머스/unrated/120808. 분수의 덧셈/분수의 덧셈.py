def solution(denum1, num1, denum2, num2):
    a= denum1*num2+denum2*num1 # 분자
    b= num1*num2 #분모
    c=1

    for i in range(1,a+1,1):
        if a%i==0: #분자가 i로 나누어떨어지면 분모도 나눌수 있는지 확인
            if b%i==0: #분모도 나눠지면
                c=i # c=최대공약수
    A=a/c
    B=b/c
    answer = A,B
    return answer