# N의 약수 찾기
def solution(n):
    for i in range(1,n+1):
        if not n % i:
            print(i)

if __name__ == "__main__":
    solution(int(input('enter number : ')))