#정수 제곱근 판별
def solution(n):
    return -1 if int(str(n**(1/2)).split(".")[1]) else (int(str(n**(1/2)).split(".")[0])+1)**2

#다른 사람 풀이
def nextSqure(n):
    return n == int(n**.5)**2 and int(n**.5+1)**2 or -1