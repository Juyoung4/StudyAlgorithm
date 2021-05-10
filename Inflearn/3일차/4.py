# 두 리스트 합치기
"""
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로그램 작성

[INPUT]
첫 번째 줄에 첫 번째 리스트의 크기 N(1<=N<=100)이 주어집니다.
두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어집니다.
세 번째 줄에 두 번째 리스트의 크기 M(1<=M<=100)이 주어집니다.
네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어집니다.
각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.

[OUTPUT]
오름차순으로 정렬된 리스트를 출력합니다.

[INPUT EX]
3
1 3 5
5
2 3 6 7 9

[OUTPUT EX]
1 2 3 3 5 6 7 9
"""
import time

def solution():
    len_a = int(input())
    a = list(map(int, input().split()))
    len_b = int(input())
    b = list(map(int, input().split()))
    
    return sorted(a+b)

def solution2():
    n=int(input())
    a=list(map(int, input().split()))
    m=int(input())
    b=list(map(int, input().split()))
    p1=p2=0
    c=[]
    while p1<n and p2<m:
        if a[p1]<b[p2]:
            c.append(a[p1])
            p1+=1
        else:
            c.append(b[p2])
            p2+=1
    if p1<n:
        c=c+a[p1:]
    if p2<m:
        c=c+b[p2:]
    return c

if __name__ == "__main__":
    # WorkingTime1: 2.9754538536071777 sec
    start_time = time.time()
    print(solution())
    end_time = time.time()
    print("WorkingTime1: {} sec".format(end_time-start_time))

    # WorkingTime2: 2.18285870552063 sec
    start_time = time.time()
    print(solution2())
    end_time = time.time()
    print("WorkingTime2: {} sec".format(end_time-start_time))