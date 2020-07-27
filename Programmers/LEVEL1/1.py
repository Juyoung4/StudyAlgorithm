# 두 정수의 합
# 조건 : a==b이면 아무거나 하나 출력 [a와 b의 범위 --> 뺐움..]
def solution(a, b):
    if a == b: return a
    if a > b: a,b = b,a
    answer = 0
    for i in range(a,b+1):
        answer += i
    return answer