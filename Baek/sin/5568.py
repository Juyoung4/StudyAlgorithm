# https://www.acmicpc.net/problem/5568
# 카드 놓기

from itertools import permutations

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    cards = [input() for _ in range(n)]

    total = []
    for c in permutations(cards, k):
        temp = "".join(c)
        if temp not in total: total.append(temp)

    print(len(total))

"""
n(4 ≤ n ≤ 10)장 => 1이상 99이하의 정수
이 카드 중에서 k(2 ≤ k ≤ 4)장을 선택하고, 가로로 나란히 정수를 만들기

"""