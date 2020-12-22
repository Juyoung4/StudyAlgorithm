# 1부터 N까지 소수 찾기

def solution(n):
    result = 0
    if n in (1,2,3):
        print(n)
        return

    for i in range(4,n+1):
        for j in range(2, i+1):
            if not i % j: break
        if i == j: print(i)

    return result

if __name__ == "__main__":
    solution(int(input('enter number : ')))