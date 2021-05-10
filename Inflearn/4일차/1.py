# 이분 검색

"""
N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한 개의 수인 M이 주어지면 
이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는 프로그램을 작성하세요. 
단 중복값은 존재하지 않습니다.

[INPUT]
첫 줄에 한 줄에 자연수 N(3<=N<=1,000,000)과 M이 주어집니다
두 번째 줄에 N개의 수가 공백을 사이에 두고 주어집니다.

[OUTPUT]
첫 줄에 정렬 후 M의 값의 위치 번호를 출력한다.


[INPUT EX]
8 32
23 87 65 12 57 32 99 81

[OUTPUT EX]
3
"""

import time

def solution(M, l):
    start, end = 0, len(l) - 1
    while start <= end:
        m = (start + end)//2
        if l[m] < M:
            start = m + 1
        elif l[m] > M:
            end = m - 1
        else:
            return m+1

def solution2(M, l, start, end):
    m = (start+end)//2
    if l[m] == M: return m+1
    elif l[m] < M: start = m+1
    else: end = m - 1
    return solution2(M, l, start, end)

def solution3(N, M, l):
    return 


if __name__ == "__main__":
    N, M = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    start, end = 0, len(l) - 1

    start_time = time.time()
    print(solution(M, l))
    end_time = time.time()
    print("WorkingTime1: {} sec".format(end_time-start_time))

    start_time = time.time()
    print(solution2(M, l, start, end))
    end_time = time.time()
    print("WorkingTime2: {} sec".format(end_time-start_time))