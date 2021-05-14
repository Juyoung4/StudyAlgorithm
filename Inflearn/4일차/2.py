# 2. 결정 알고리즘 - 랜선 자르기

"""
1 <= k <= 10000 / 1 <= N <= 1000000
K개 랜선 가짐 
  -> 모두 N개의 같은 길이의 랜선을 만들고 싶음
  ->  K개의 랜선을 잘라서 만들어야 함

* 만들 수 있는 최대 랜선의 길이 구하기
"""

def counts(lines, len_, N):
    count = 0
    for l in lines:
        count += l//len_
    return count

def solution(K, N, lines, maxs):
    start, end = 1, maxs
    result = 0
    while start <= end:
        mid = (start+end)//2
        if counts(lines, mid, N) >= N:
            start = mid+1
            result = mid
        else:
            end = mid-1

    return result


if __name__ == "__main__":
    
    K, N = map(int, input().split())
    maxs = 10000
    lines = []
    for _ in range(K):
        temp = int(input())
        maxs = max(maxs, temp)
        lines.append(temp)

    print(solution(K, N, lines, maxs))