# N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력

"""
[INPUT]
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
각 자연수의 크기는 10,000,000를 넘지 않는다.
[OUTPUT]
자릿수의 합이 최대인 자연수를 출력한다

[INPUT EX]
3
125 15232 97

[OUTPUT EX]
97
"""

def solution(num):
    nums = input().split()
    if num != len(nums): return -1
    max_, idx_ = 0, 0
    for idx, num in enumerate(nums):
        total = 0
        for j in num:
            total += int(j)
        if total > max_: max_, idx_ = total, idx
    return nums[idx_]
        

if __name__ == "__main__":
    num = int(input())
    print(solution(num))