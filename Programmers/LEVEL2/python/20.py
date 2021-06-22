# n개의 최소공배수
def LCS(a, b):
    if b>a: a, b = b, a
    while b > 0:
        a, b = b, a%b
    return a
def solution(arr):
    answer = arr[0]
    # 최소공배수 = a*b/lcs(a, b)
    for a in arr:
        answer = answer*a / LCS(answer, a)
    
    return answer