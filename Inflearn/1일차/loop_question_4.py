# N의 약수 찾기
def solution(n):
    count = 0
    for i in range(1,n+1):
        if not n % i:
            count += 1
            print(i)
    return count

if __name__ == "__main__":
    print(solution(int(input('enter number : '))))