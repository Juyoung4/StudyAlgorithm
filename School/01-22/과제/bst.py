n = int(input())
answer = [-1 for i in range(n+1)]

def bst(n):
    if n == 1: return 1
    elif n == 2: return 1
    else:
        answer[0] = 0
        answer[1] = 0
        answer[2] = 2
        m = 3
        for i in range(3, n+1):
            answer[i] = answer[i-1] + (m**(i-2))
        #print(answer)
        return answer[-1]
print(bst(n))