# 봉우리

"""
지도 정보가 N*N 격자판에 주어집니다. 각 격자에는 그 지역의 높이가 쓰여있습니다. 
각 격자판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다.
봉우리 지역이 몇 개 있는 지 알아내는 프로그램을 작성하세요. 
격자의 가장자리는 0으로 초기화 되었다고 가정한다.
만약 N=5 이고, 격자판의 숫자가 다음과 같다면 봉우리의 개수는 10개입니다.


[INPUT]
첫 줄에 자연수 N이 주어진다.(1<=N<=50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는다.

[OUTPUT]
봉우리의 개수를 출력하세요.

[INPUT EX]
5
5 3 7 2 3
3 7 1 6 1
7 2 5 3 4
4 3 6 4 1
8 7 3 5 2

[OUTPUT EX]
10
"""

import time

def solution(N):
    matrix = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    for i in range(N):
        for j in range(N):
            if i - 1 >= 0:
                if matrix[i][j] <= matrix[i-1][j]: continue
            if i + 1 <= N-1:
                if matrix[i][j] <= matrix[i+1][j]: continue
            if j - 1 >= 0:
                if matrix[i][j] <= matrix[i][j-1]: continue
            if j + 1 <= N-1:
                if matrix[i][j] <= matrix[i][j+1]: continue
            
            total += 1
    return total
            
def solution2(n):
    dx=[-1, 0, 1, 0]
    dy=[0, 1, 0, -1]
    
    a=[list(map(int, input().split())) for _ in range(n)]

    # 가장 자리 0으로 채우기
    a.insert(0, [0]*n)
    a.append([0]*n)
    for x in a:
        x.insert(0, 0)
        x.append(0)
    
    # 봉우리 계산
    cnt=0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
                cnt+=1
    return cnt


if __name__ == "__main__":
    # WorkingTime1: 2.9966254234313965 sec
    start_time = time.time()
    print(solution(int(input())))
    end_time = time.time()
    print("WorkingTime1: {} sec".format(end_time-start_time))

    # WorkingTime2: 2.9966254234313965 sec
    start_time = time.time()
    print(solution2(int(input())))
    end_time = time.time()
    print("WorkingTime2: {} sec".format(end_time-start_time))