# 2036- 수열의 점수

if __name__ == "__main__":
    N = int(input())

    plus = []
    minus = []
    total = 0

    for _ in range(N):
        n = int(input())
        if n < 0:
            minus.append(n)
        else:
            plus.append(n)

    len_minus, len_plus = len(minus), len(plus)
    minus.sort()
    plus.sort(reverse=True)
    # 음수 계산

    for i in range(0, len_minus, 2):
        if i == len_minus-1:
            total += minus[i]
        else: 
            total += (minus[i]*minus[i+1])
    
    # 양수 계산
    for i in range(0, len_plus, 2):
        if i == len_plus-1:
            total += plus[i]
        else:
            if plus[i] == 1 or plus[i+1] == 1:
                total += (plus[i]+plus[i+1])
            else:
                total += (plus[i]*plus[i+1])

    print(total)



"""
heapq 사용한 겨웅
import heapq
if __name__ == "__main__":
    N = int(input())

    plus = []
    minus = []
    total = 0

    for _ in range(N):
        n = int(input())
        if n == 0: continue
        if n < 0:
            heapq.heappush(minus, n)
        else:
            heapq.heappush(plus, -n)

    len_minus, len_plus = len(minus), len(plus)
    # 음수 계산
    for i in range(len_minus//2):
        total += (heapq.heappop(minus)*heapq.heappop(minus))
    if len_minus%2 != 0: # 홀수이면
        total += heapq.heappop(minus)
    
    # 양수 계산
    for i in range(len_plus//2):
        n1 = -heapq.heappop(plus)
        n2 = -heapq.heappop(plus)
        if n1 == 1 or n2 == 1:
            total += (n1+n2)
        else:
            total += (n1*n2)
    if len_plus%2 != 0: # 홀수이면
        total += -heapq.heappop(plus)
    print(total)

"""