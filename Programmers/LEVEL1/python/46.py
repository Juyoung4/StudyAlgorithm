# 46. Summer/Winter Coding 소수 만들기
from itertools import combinations

def check(num):
    checks = [False]*(num+1)
    for i in range(2, num+1):
        for j in range(i*2, num+1, i):
            if not checks[j]: checks[j] = True
    return checks

def solution(nums):
    answer = 0
    combi = [sum(c) for c in combinations(nums, 3)]
    result = check(max(combi))
    for c in combi:
        if not result[c]: answer += 1
    return answer

"""
다른 사람풀이
from itertools import combinations
def prime_number(x):
    answer = 0
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            answer+=1
    return 1 if answer==1 else 0

def solution(nums):
    return sum([prime_number(sum(c)) for c in combinations(nums,3)])

"""