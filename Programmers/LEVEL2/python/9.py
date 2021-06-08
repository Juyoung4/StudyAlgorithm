# 9. H-Index
def solution(citations):
    for idx in range(max(citations), -1, -1):
        count = 0
        for c in citations:
            if c >= idx: count += 1
        if count >= idx: return idx

print(solution([3, 0, 6, 1, 5]))

"""
H-Index : 논문 n편 중, 
       h <= h번 이상 인용된 논문이 /
       나머지 논문(인용x) <= h
       => h의 최댓값 = H-Index이다

[ex] [3, 0, 6, 1, 5]
sort = [0, 1, 3, 5, 6] / [4, 100, 101, 102, 150]
n = 5, 
    3 -> 3 >= h=3, 3개 / 2개 <= 3
    
"""

"""
다른 사람 풀이
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
"""