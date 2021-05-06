#x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    if n <= 0 or n > 1000: return
    return [x*i for i in range(1,n+1)]

# 다른 사람 풀이
def number_generator(x, n):
    t = list(range(x, n*x+1, x))
    return t

#range 함수를 이용해서 풀이