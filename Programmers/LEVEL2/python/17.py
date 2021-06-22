def solution(n):
    n = bin(n)[2:][::-1]
    len_n = len(n)
    one = n.count("1")
    print(n)
    if one == len_n:
        return int("1"+"0"+"1"*(len_n-1), 2)
    start, end = -1, -1
    for idx in range(len_n):
        if n[idx] == "0" and start >= 0:
            end = idx
            break
        if n[idx] == "1" and start == -1:
            start = idx
    temp = ""
    if end == -1: 
        cnt = one-1
        end = len_n
    else: 
        cnt = end-start-1
    for i in range(end):
        if cnt > 0:
            temp += "1"
            cnt -= 1
        else:
            temp += "0"
    
    if end == -1:
        return int("1"+temp[::-1], 2)
    else:
        return int(n[idx+1:][::-1]+"1"+temp[::-1], 2)

print(solution(29))

"""
다른 사람 풀이 -> 완탐

def solution(n):
    c = bin(n).count('1')
    for m in range(n+1,1000001):
        if bin(m).count('1') == c:
            return m

"""