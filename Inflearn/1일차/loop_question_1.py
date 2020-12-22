# 1부터 N까지 홀수 출력하기

def solution(n):
    for i in range(1,n+1):
        if i % 2 != 0: print(i)

if __name__ == "__main__":
    solution(int(input('enter number : ')))