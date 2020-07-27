# 두 정수의 합
# 조건 : a==b이면 아무거나 하나 출력 [a와 b의 범위 --> 뺐움..]
def solution(a, b):
    if a == b: return a
    if a > b: a,b = b,a
    answer = 0
    for i in range(a,b+1):
        answer += i
    return answer



#다른 사람의 답
def adder(a, b):
    # 함수를 완성하세요
    if a > b: a, b = b, a
    return sum(range(a,b+1))


def adder(a, b):
    # 함수를 완성하세요
    return sum(range(min(a,b),max(a,b)+1))


