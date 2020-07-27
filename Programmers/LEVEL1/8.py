#나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    a=[i for i in arr if i%divisor==0]
    a.sort()
    return a if a else [-1]

#다른 사람 풀이


def solution(arr, divisor): 
    return sorted([n for n in arr if n%divisor == 0]) or [-1]

#위에 코드를 한줄로 
