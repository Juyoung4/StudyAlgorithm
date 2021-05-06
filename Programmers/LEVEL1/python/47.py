# 47. 월간 코드 챌린지 시즌1 3진법 뒤집기

def solution(n):
    answer = ''
    while n != 0:
        answer += str(n%3)
        n = n//3
    answer = int(answer)
    total = 0
    idx = 0

    while answer != 0:
        if idx == 0: 
            total += (answer%10)
        else:
            total += (answer%10)*(3**idx)
        answer = answer//10
        idx += 1

    return total

"""
다른 사람 풀이
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

"""