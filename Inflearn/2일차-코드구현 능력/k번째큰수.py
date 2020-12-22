# 1부터 100사이의 자연수가 적힌 N장의 카드(중복 카드도 있음)에서 3장을 뽑아 각 카드에 적힌 수를 합한 값 기록
# 3장을 뽑을 수 있는 모든 경우를 기록 -> 기록한 값 중 K번째로 큰 수를 출력하는 프로그램을 작성

"""
[INPUT]
첫 줄에 자연수 N(3<=N<=100)과 K(1<=K<=50) 입력되고, 그 다음 줄에 N개의 카드값이 입력 
[OUTPUT]
첫 줄에 K번째 수를 출력합니다. K번째 수는 반드시 존재

[INPUT EX]
10 3 -> N, K입력
13 15 34 23 45 65 33 11 26 42 -> N개의 카드값 입력됨

[OUTPUT EX]
143

"""

def solution1(N, K, card):
    if N != len(card): return -1
    # 조합 만들기
    # 1. itertools 이용
    from itertools import combinations
    card = list(map(sum, list(combinations(card, 3))))
    card.sort(reverse=True)
    return card[K-1]


if __name__ == "__main__":
    N, K = map(int, input().split())
    card = list(map(int, input().split()))
    print(solution1(N, K, card))