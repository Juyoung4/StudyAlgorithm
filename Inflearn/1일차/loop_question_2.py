# 1부터 N까지의 합 구하기

def solution(n):
    result = 0
    for i in range(1,n+1):
        result += i
    return result

if __name__ == "__main__":
    print(solution(int(input('enter number : '))))