# 42. 월간 코드 챌린지 시즌1 내적
def solution(a, b):
    answer = 0
    for i, j in zip(a, b):
        answer += i*j
    return answer

"""
다른 사람 풀이
def solution(a, b):
    return sum(map(lambda i: a[i]*b[i], range(len(a))))
"""