# 소수(에라토스테네스 체)
# 자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요

"""
[INPUT]
첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.
[OUTPUT]
첫 줄에 소수의 개수를 출력합니다.

[INPUT EX]
20

[OUTPUT EX]
8
"""


def solution(num):
    if num == 1 : return -1
    result = [True] * num
    sqr_ = int(num ** 0.5)
    for i in range(2, sqr_+1):
        if result[i]:
            for j in range(i+i, num, i):
                result[j] = False
    return len([i for i in result[2:] if i])
    
if __name__ == "__main__":
    print(solution(int(input())))
