# 약수의 합
def solution(n):
    if n < 0 and n >3000: return
    if n==0: return 0
    return n + sum([i for i in range(1, (n//2)+1) if n%i ==0])

## 반 값으로 하면 계산량 적어짐을 이용함