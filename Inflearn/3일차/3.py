# 곳감

"""
현수는 각 격자단위로 말리는 감의 수를 정합니다. 
현수는 격자의 행을 기준으로 왼쪽, 또는 오른쪽으로 회전시켜 위치를 변경해 모든 감이 잘 마르게 합니다.
만약 회전명령 정보가 2 0 3이면 2번째 행을 왼쪽으로 3만큼 아래 그림처럼 회전시키는 명령입니다.
첫 번째 수는 행번호, 두 번째 수는 방향인데 0이면 왼쪽, 1이면 오른쪽이고, 세 번째 수는 회전하는 격자의 수 이다.

M개의 회전명령을 실행하고 난 후 아래와 같이 마당의 모래시계 모양의 영역에는 감 이 총 몇 개가 있는지 출력하는 프로그램을 작성하세요.

[INPUT]
첫 줄에 자연수 N(3<=N<=20) 이 주어며, N은 홀수입니다.
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
이 자연수는 각 격자안에 있는 감의 개수이며, 각 격자안의 감의 개수는 100을 넘지 않는다.
그 다음 줄에 회전명령의 개수인 M(1<=M<=10)이 주어지고, 그 다음 줄부터 M개의 회전명령
정보가 M줄에 걸쳐 주어집니다.

[OUTPUT]
총 감의 개수를 출력합니다.

[INPUT EX]
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
3 # 회전 개수
2 0 3
5 1 2
3 1 4

[OUTPUT EX]
362
"""

import time

def solution(N):
    matrix = [list(map(int, input().split())) for _ in range(N)]
    num = int(input())
    for _ in range(num):
        a, b, c = map(int, input().split())
        import copy
        d = copy.deepcopy(matrix)
        for j in range(N):
            if b == 1:
                # a[h-1].append(a[h-1].pop())
                if j+c >= N-1:
                    matrix[a-1][j+c-N] = d[a-1][j]
                else:
                    matrix[a-1][j+c] = d[a-1][j]
            else:
                # a[h-1].insert(0, a[h-1].pop())
                matrix[a-1][j-c] = d[a-1][j]
        del d
    total = 0
    left,right = 0,N
    for i in range(N):
        print(left, right, matrix[i][left:right])
        total += sum(matrix[i][left:right])
        if i < N//2:
            left += 1
            right -= 1
        else:
            left -= 1
            right += 1
    return total


def solution2(n):
    a=[list(map(int, input().split())) for _ in range(n)]
    m=int(input())
    for i in range(m):
        h, t, k=map(int, input().split())
        if(t==0):
            for _ in range(k):
                a[h-1].append(a[h-1].pop(0))
        else:
            for _ in range(k):
                a[h-1].insert(0, a[h-1].pop())
    
    res=0
    s=0
    e=n-1
    for i in range(n):
        for j in range(s, e+1):
            res+=a[i][j]
        if i<n//2:
            s+=1
            e-=1
        else:
            s-=1
            e+=1
    return res


if __name__ == "__main__":
    # WorkingTime1: 1.1167099475860596 sec
    start_time = time.time()
    print(solution(int(input())))
    end_time = time.time()
    print("WorkingTime1: {} sec".format(end_time-start_time))

    # WorkingTime2: 1.5906453132629395 sec
    start_time = time.time()
    print(solution2(int(input())))
    end_time = time.time()
    print("WorkingTime2: {} sec".format(end_time-start_time))