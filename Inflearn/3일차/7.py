# 수들의 합

"""
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의
합 A[i]+A[i+1]+…+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오

[INPUT]
첫째 줄에 N(1≤N≤10,000), M(1≤M≤300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], …,
A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.

[OUTPUT]
첫째 줄에 경우의 수를 출력한다.

[INPUT EX]
8 3
1 2 1 3 1 1 1 2

[OUTPUT EX]
5
"""

import time

def solution():
    len_, num = map(int, input().split())
    nums = list(map(int, input().split()))
    if len_ != len(nums): return -1
    count = 0
    for i in range(len(nums)):
        sum_ = nums[i]
        if sum_ == num: 
            count += 1
            continue
        for j in range(i+1,len(nums)):
            sum_ += nums[j]
            if sum_ > num: break
            if sum_ == num:
                count += 1
                break
    return count
        
def solution2():
    n, m=map(int, input().split())
    a=list(map(int, input().split()))
    lt=0
    rt=1
    tot=a[0]
    cnt=0
    while True:
        if tot<m:
            if rt<n:
                tot+=a[rt]
                rt+=1
            else:
                break
        elif tot==m:
            cnt+=1
            tot-=a[lt]
            lt+=1
        else:
            tot-=a[lt]
            lt+=1
    return cnt

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