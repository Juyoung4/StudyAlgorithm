# 숫자의 표현

def solution(n):
    answer = 1
    if n == 1 or n == 2: return answer
    
    mid = n//2+1

    for i in range(1, mid+1):
        temp = 0
        for j in range(i, mid+1):
            if temp+j < n:
                temp += j
            elif temp+j == n:
                answer += 1
                break
            else:
                break
            
    return answer

print(solution(15))