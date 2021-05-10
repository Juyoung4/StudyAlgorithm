# 점수 계산
"""
[문제]
 여러 개의 OX 문제로 만들어진시험에서 연속적으로 답을 맞히는 경우에는 가산점을 주기 위해서 다음과 같이 점수 계산을 하기로 하였다
 
 - 1번 문제가 맞는 경우에는 1점으로 계산한다.
 - 앞의 문제에 대해서는 답을 틀리다가 답이 맞는 처음 문제는 1점으로 계산한다.
 -  연속으로 문제의 답이 맞는 경우에서 두 번째 문제는 2점, 세 번째 문제는 3점, ..., K번째 문제는 K점으로 계산한다.
 - 틀린 문제는 0점으로 계산한다.

 (ex)
  10 개의 OX 문제에서 답이 맞은 문제의 경우에는 1로 표시하고, 틀린 경우에는 0으로 표시하여
    1011100110일때 점수 계산하는 방법은
    1012300120 => 1+1+2+3+1+2=10 점이다.

[INPUT EX]
10
1 0 1 1 1 0 0 1 1 0

[OUTPUT EX]
10
"""

def solution(T):
    score = list(map(int, input().split()))
    if len(score) != T: return -1
    add_ = 1 if score[0] else 0
    total = 1 if score[0] else 0
    for i in range(1, len(score)):
        if not score[i]:
            add_ = 0
            print(add_, total)
            continue
        if not score[i-1] and score[i]: 
            add_ = 1
            total += add_
            print(add_, total)
            continue
        if score[i-1] and score[i]:
            add_ += 1
            total += add_
            print(add_, total)
            continue
    return total
            
if __name__ == "__main__":
    print(solution(int(input())))