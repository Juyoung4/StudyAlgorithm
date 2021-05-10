# 정다면체
# 두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확률이 높은 숫자를 출력하는 프로그램을 작성하세요.
# 정답이 여러 개일 경우 오름차순으로 출력합니다.

"""
[INPUT]
첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.

[OUTPUT]
첫 번째 줄에 답을 출력합니다.


[INPUT EX]
4 6

[OUTPUT EX]
5 6 7
"""

def solution(input_):
    N, M = map(int, input_.split())
    result = dict()
    for i in range(1, N+1):
        for j in range(1, M+1):
            temp = i+j
            if temp not in result.keys():
                result[temp] = 1
            else:
                result[temp] += 1
    result = [k for k,v in result.items() if v == max(result.values())]
    return sorted(result)

if __name__ == "__main__":
    input_ = input()
    print(solution(input_))