def solution(n):
    if n == 1: return 1
    end = 0
    m = n//2
    answer = 0
    for i in range(m):
        start, end = end+1, end + (n-1-2*i)*4
        mid = (start+end)//2+1
        answer += (start + mid)
    if n%2 != 0: # 홀수면 추가
        answer += n*n
    return answer

n1 = 5
ret1 = solution(n1)

print("solution 함수의 반환 값은", ret1, "입니다.")
    
n2 = 2
ret2 = solution(n2)

print("solution 함수의 반환 값은", ret2, "입니다.")

n2 = 4
ret2 = solution(n2)

print("solution 함수의 반환 값은", ret2, "입니다.")