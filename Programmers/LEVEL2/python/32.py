# 32. 짝지어서 제거하기
from collections import deque

def solution(s):
    len_s = len(s)
    if len_s < 2: return 0
    if len_s == 2:
        if s[0] == s[1]: return 1
        else: return 0
    if len_s % 2: return 0
    
    queue = deque()
    
    for i in range(len_s):
        if not queue or queue[-1] != s[i]: queue.append(s[i])
        else: queue.pop()

    if queue: return 0
    else: return 1

print(solution('cdcd'))