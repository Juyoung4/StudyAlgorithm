from collections import deque

def solution(n, k, cmd):
    answer = ''
    stack = [0]*(n)
    deletes = deque()
    start = 0
    end = n-1
    for c in cmd:
        if c == 'C':
            deletes.append(k)
            stack[k] = 1
            if k == end:
                end -= 1
                k -= 1# 삭제하고 바로 윗줄 선택
            elif k == start:
                start += 1
                k += 1
            else: k += 1
        elif c == 'Z':
            if not deletes: continue
            d = deletes.pop()
            stack[d] = 0
        else:
            a, b = c.split()
            b = int(b)
            if a == "U":
                if k-b <= 0: k = 0
                else:
                    temp = sum(stack[k-b:k+1])
                    if k-temp-b <= 0: k = start
                    else: k -= (temp+b)
            else:
                if k+b >= n-1: k = n-1
                else:
                    temp = sum(stack[k:k+b+1])
                    if k+temp+b >= n-1: k = end
                    else: k += (temp+b)
    for s in stack:
        if s: answer += 'X'
        else: answer += 'O'
    return answer