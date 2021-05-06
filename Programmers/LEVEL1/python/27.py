#콜라츠 추측
# def solution(num):
#     if num == 1: return 0
#     else:
#         return 1 + solution(num//2) if not num % 2 else 1 + solution(num*3 + 1)

def solution(num):
    total = 0
    while num != 1:
        if total > 500: 
            total = -1
            break
        if not num % 2: 
            total += 1
            num = num //2
        else: 
            total += 1
            num = num*3 + 1
    return total

# 다른 사람 풀이
def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1