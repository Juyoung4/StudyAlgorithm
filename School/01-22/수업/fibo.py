n = int(input())
answer = [-1 for i in range(n)]

def fibo(n):
    if n == 1: return 1
    elif n == 2: return 1
    else:
        answer[0] = 1
        answer[1] = 1
        for i in range(2, n):
            answer[i] = answer[i-1] + answer[i-2]
        return answer[-1]
print(fibo(n))