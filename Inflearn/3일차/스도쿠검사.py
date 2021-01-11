# 스도쿠검사

"""
위 그림은 스도쿠를 정확하게 푼 경우이다. 
각 행에 1부터 9까지의 숫자가 중복 없이 나오고, 각 열에 1부터 9까지의 숫자가 중복 없이 나오고
각 3×3짜리 사각형(9개이며, 위에서 색깔로 표시되었다)에 1부터 9까지의 숫자가 중복 없이 나오기 때문이다.
완성된 9×9 크기의 수도쿠가 주어지면 정확하게 풀었으면 “YES", 잘 못 풀었으면 ”NO"를 출력하는 프로그램을 작성하세요.


[INPUT]
첫 번째 줄에 완성된 9×9 스도쿠가 주어집니다.

[OUTPUT]
첫째 줄에 “YES" 또는 ”NO"를 출력하세요.

[INPUT EX]
1 4 3 6 2 8 5 7 9
5 7 2 1 3 9 4 6 8
9 8 6 7 5 4 2 3 1
3 9 1 5 4 2 7 8 6
4 6 8 9 1 7 3 5 2
7 2 5 8 6 3 9 1 4
2 3 7 4 8 1 6 9 5
6 1 9 2 7 5 8 4 3
8 5 4 3 9 6 1 2 7

[OUTPUT EX]
YES
"""

import time

def solution():
    matrix = [list(map(int, input().split())) for _ in range(9)]
    for i in range(9):
        if len(set(matrix[i])) != 9 : return "NO!"
        if len(set(j[0] for j in matrix)) != 9: return "NO!"

    count = 0
    for i in range(3):
        for _ in range(3):
            if count >= 9: count = 0
            temp = [matrix[p][k] for k in range(count, count+3) for p in range(i*3,i*3+3)]
            if len(set(temp)) != 9: return "NO!"
            count += 3
    return "Yes"
            
def solution2():
    a=[list(map(int, input().split())) for _ in range(9)]
    for i in range(9):
        ch1=[0]*10
        ch2=[0]*10
        for j in range(9):
            ch1[a[i][j]]=1
            ch2[a[j][i]]=1
        if sum(ch1)!=9 or sum(ch2)!=9:
            return "NO!"
    for i in range(3):
        for j in range(3):
            ch3=[0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3)!=9:
                return "NO!"
    return "Yes"

if __name__ == "__main__":
    # WorkingTime1: 0.7551536560058594 sec
    start_time = time.time()
    print(solution())
    end_time = time.time()
    print("WorkingTime1: {} sec".format(end_time-start_time))

    # WorkingTime2: 0.5106456279754639 sec
    start_time = time.time()
    print(solution2())
    end_time = time.time()
    print("WorkingTime2: {} sec".format(end_time-start_time))