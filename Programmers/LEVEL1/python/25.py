#소수 찾기
"""
에라토스테네스의 체 이용
# 1 제거
# 먼저 짝수는 약수 불가 -> 짝수 모두 제거
# 홀수에서 첫번째 원소로 나눠 지는거 모두 제거
"""
def solution(n):
    a = set([i for i in range(3, n+1, 2)])
    for i in range(3, n+1 ,2):
        if i in a:
            a -= set([i for i in range(i*2,n+1,i)])
    print(a)
    return len(a)+1
    
print(solution(10))

