# 주사위 게임
"""
[문제]
1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다.
규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다.
규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다. 

N 명이 주사위 게임에 참여하였을 때, 가장 많은 상금을 받은 사람의 상금을 출력하는 프로그램 작성

[INPUT EX]
3
3 3 6
2 2 2
6 2 5

[OUTPUT EX]
12000
"""
import time

def solution1(T):
    max_ = 0
    for i in range(T):
        temp = list(map(int, input().split()))
        price = 0
        if len(set(temp)) == 3:
            price = max(temp)*100
            max_ = price if max_ < price else max_
            continue
        if len(set(temp)) == 2:
            price = [i for i in temp if temp.count(i) > 1][0]*100 + 1000
            max_ = price if max_ < price else max_
            continue
        if len(set(temp)) == 1:
            price = temp[0]*1000 + 10000
            max_ = price if max_ < price else max_
            continue
    return max_

def solution2(T):
    res=0
    for i in range(T):
        tmp=input().split() 
        tmp.sort() 
        a, b, c=map(int, tmp)
        if a==b and b==c:
            money=10000+(a*1000);
        elif a==b or a==c:
            money=1000+(a*100)
        elif b==c:
            money=1000+(b*100)
        else:
            money=c*100
        if money > res:
            res=money
    return res

if __name__ == "__main__":
    start = time.time()
    print(solution1(int(input())))
    print("solution1 time :", time.time() - start)

    start = time.time()
    print(solution2(int(input())))
    print("solution2 time :", time.time() - start)

    ## solution1 time이 더 짧음
