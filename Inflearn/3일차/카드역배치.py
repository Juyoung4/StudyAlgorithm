# 카드 역 배치

"""
1부터 20까지 숫자가 하나씩 쓰인 20장의 카드가 아래 그림과 같이 오름차순으로 한 줄로 놓여있다. 
각 카드의 위치는 카드 위에 적힌 숫자와 같이 1부터 20까지로 나타낸다.
다음과 같은 규칙으로 카드의 위치를 바꾼다:
[1] 구간 [a, b] (단, 1 ≤ a ≤ b ≤ 20)가 주어지면 위치 a부터 위치 b까지의 카드를 현재의 역순으로 놓는다
(ex) 1,2,3,4,10,9,8,7,6,5,11,12,13,14,15,16,17,18,19,20
구간이 [5, 10]으로 주어진다면, 5부터 위치 10까지의 카드 5, 6, 7, 8, 9, 10을 역순으로 하여 10, 9, 8, 7, 6, 5로 놓는다. 

순서를 뒤집는 작업을 연속해서 처리한 뒤 마지막 카드들의 배치를 구하는 프로그램을 작성

[INPUT]
총 10개의 줄에 걸쳐 한 줄에 하나씩 10개의 구간이 주어진다.

[OUTPUT]
마지막 카드들의 배치를 한 줄에 출력한다

[INPUT EX]
5 10
9 13
1 2
3 4
5 6
1 2
3 4
5 6
1 20
1 20

[OUTPUT EX]
1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20
"""

import time

def solution(N):
    result = list(range(21))
    #result = [str(i) for i in range(1,21)]
    for _ in range(N):
        a,b = map(int, input().split())
        result = result[:a-1] + result[a-1:b][::-1] + result[b:]
    #return " ".join(result)
    return result
        
def solution2(N):
    result = list(range(21))
    for _ in range(N):
        s, e=map(int, input().split())
        # swap방식 이용
        for i in range((e-s+1)//2): # (e-s+1)//2 ->
            result[s+i], result[e-i]=result[e-i], result[s+i]
    result.pop(0)
    return result

if __name__ == "__main__":
    # WorkingTime1: 2.9754538536071777 sec
    start_time = time.time()
    print(solution(10))
    end_time = time.time()
    print("WorkingTime1: {} sec".format(end_time-start_time))

    # WorkingTime2: 2.18285870552063 sec
    start_time = time.time()
    print(solution2(10))
    end_time = time.time()
    print("WorkingTime2: {} sec".format(end_time-start_time))