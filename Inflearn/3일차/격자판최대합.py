# 격자판 최대합

"""
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력

[INPUT]
첫 줄에 자연수 N이 주어진다.(1<=N<=50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는다

[OUTPUT]
최대합을 출력합니다.


[INPUT EX]
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

[OUTPUT EX]
155
"""

import time

def solution(N):
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_ =-2147000000
    sum1, sum2 = 0,0
    for i in range(N):
        sum3, sum4 = 0, 0
        for j in range(N):
            sum3 += matrix[i][j]
            sum4 += matrix[j][i]
        if max_ < sum3: max_ = sum3
        if max_ < sum4: max_ = sum4

        sum1 += matrix[i][i] # 대각선
        if max_ < sum1: max_ = sum1

        sum2 += matrix[i][N-i-1] # 반대쪽 대각선
        if max_ < sum2: max_ = sum2
    return max_

def solution2(n):
    a=[list(map(int, input().split())) for _ in range(n)]
    largest=-2147000000
    for i in range(n):
        sum1=sum2=0
        for j in range(n):
            sum1+=a[i][j]
            sum2+=a[j][i]
        if sum1>largest:
            largest=sum1
        if sum2>largest:
            largest=sum2
    sum1=sum2=0
    for i in range(n):
        sum1+=a[i][i]
        sum2+=a[i][n-i-1]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2
    return largest

if __name__ == "__main__":
    # WorkingTime1: 3.979116439819336 sec
    start_time = time.time()
    print(solution(int(input())))
    end_time = time.time()
    print("WorkingTime1: {} sec".format(end_time-start_time))

    # WorkingTime2: 6.3520591259002686 sec
    start_time = time.time()
    print(solution2(int(input())))
    end_time = time.time()
    print("WorkingTime2: {} sec".format(end_time-start_time))