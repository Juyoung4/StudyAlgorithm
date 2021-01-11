# 격자판 회문수

"""
1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서 가로방향 또는
세로방향으로 길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하세요.
회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.

[INPUT]
1부터 9까지의 자연수로 채워진 7*7격자판이 주어집니다.

[OUTPUT]
5자리 회문수의 개수를 출력합니다.

[INPUT EX]
2 4 1 5 3 2 6
3 5 1 8 7 1 7
8 3 2 7 1 3 8
6 1 2 3 2 1 1
1 3 1 3 5 3 2
1 1 2 5 6 5 2
1 2 2 2 2 1 5

[OUTPUT EX]
3
"""

import time

def solution():
    matrix = [list(map(int, input().split())) for _ in range(7)]
    total = 0
    for i in range(7):
        temp = [k[i] for k in matrix]
        for j in range(3):
            temp2 = temp[j:j+5][::-1]
            if temp2 == temp[j:j+5]: 
                total += 1
            temp3 = matrix[i][j:j+5][::-1]
            if matrix[i][j:j+5] == temp3: 
                total += 1
        del temp, temp2, temp3
    return total

def solution2():
    board=[list(map(int, input().split())) for _ in range(7)]
    cnt=0
    for i in range(3):
        for j in range(7):
            tmp=board[j][i:i+5]
            if tmp==tmp[::-1]:
                cnt+=1
            for k in range(2):
                if board[i+k][j]!=board[i+5-k-1][j]:
                    break
            else:
                cnt+=1
    return cnt

if __name__ == "__main__":
    start_time = time.time()
    print(solution2())
    end_time = time.time()
    print("WorkingTime2: {} sec".format(end_time-start_time))

    start_time = time.time()
    print(solution())
    end_time = time.time()
    print("WorkingTime1: {} sec".format(end_time-start_time))