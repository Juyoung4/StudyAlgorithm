# 사과나무

"""
현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어저있다.
N의 크기는 항상 홀수이다.
가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사과를 수확할 때 다이아몬드 모양의 
격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서 남겨놓는다.

[INPUT]
첫 줄에 자연수 N(홀수)이 주어진다.(3<=N<=20)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
이 자연수는 각 격자안에 있는 사과나무에 열린 사과의 개수이다.
각 격자안의 사과의 개수는 100을 넘지 않는다

[OUTPUT]
수확한 사과의 총 개수를 출력합니다.

[INPUT EX]
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

[OUTPUT EX]
379
"""
import time

def solution(N):
    apple = [list(map(int, input().split())) for _ in range(N)]
    count, total = 1, 0
    for i in range(len(apple)):
        total += apple[i][N//2]
        if count//2:
            for j in range(1, (count//2) +1):
                total += apple[i][N//2 + j]
                total += apple[i][N//2 - j]
        if i >= (N//2):
            count -= 2
        else:
            count += 2
    return total

def solution2(N):
    apple = [list(map(int, input().split())) for _ in range(N)]
    res=0
    s=e=N//2
    for i in range(N):
        for j in range(s, e+1):
            res+=apple[i][j]
        if i<N//2:
            s-=1
            e+=1
        else:
            s+=1
            e-=1
    return res

if __name__ == "__main__":
    # WorkingTime1: 1.082160472869873 sec
    start_time = time.time()
    print(solution(int(input())))
    end_time = time.time()
    print("WorkingTime1: {} sec".format(end_time-start_time))

    # WorkingTime2: 1.529926061630249 sec
    start_time = time.time()
    print(solution2(int(input())))
    end_time = time.time()
    print("WorkingTime2: {} sec".format(end_time-start_time))