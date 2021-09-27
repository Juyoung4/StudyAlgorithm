# (2019 카카오 개발자 겨울 인턴쉽) 튜플

import re

def solution(s):
    answer = []
    s = s[1:-1]

    numbers = []
    for num in re.findall("{[0-9,?]+}", s):
        if "," not in num:
            numbers.insert(0, [int(num[1:-1])])
        else:
            numbers.append(list(map(int, num[1:-1].split(","))))
    
    if len(numbers) == 1: return numbers[0]
    numbers = sorted(numbers, key = lambda x : len(x))
    
    tuples = [numbers[0][0]]
    for nums in numbers[1:]:
        tuples.append(list(set(nums)-set(tuples))[0])
    
    return tuples