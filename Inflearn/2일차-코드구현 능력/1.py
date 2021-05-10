# 대표 값
# N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성
# 참고: 평균과 가장 가까운 점수가 여러개 -> 점수가 높은 순, 높은 점수 여러명 -> 학생번호가 빠른 순

"""
[INPUT]
첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연수
학생의 번호는 앞에서부터 1로 시작해서 N까지이다.
[OUTPUT]
첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다.
평균은 소수 첫째 자리에서 반올림합니다.

[INPUT EX]
10
45 73 66 87 92 67 75 79 75 80

[OUTPUT EX]
74 7
"""
import numpy as np 

def solution(num):
    scores = np.array(list(map(int, input().split())))
    if num != len(scores): return -1
    mean = int(round(np.mean(scores), 0)) # 반올림 구하기 -> int((sum(scores)/num) + 0.5)하면 된다
    diff = abs(scores - mean)
    diff = [idx for idx, v in enumerate(diff) if v == min(abs(diff))]
    if len(diff) == 1: return "{} {}".format(mean , diff[0])
    diff = sorted(zip(diff, scores[np.array(diff)]), key=lambda x: (-x[1], x[0]))
    return "{} {}".format(mean , diff[0][0]+1)

if __name__ == "__main__":
    num = int(input())
    print(solution(num))