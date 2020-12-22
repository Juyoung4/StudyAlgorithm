# N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를
# 오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.

"""
[INPUT]
첫 번째 줄에 테스트 케이스 T(1<=T<=10)이 주어집니다.
    [각 케이스별]
    첫 번째 줄은 자연수 N(5<=N<=500), s, e, k가 차례로 주어진다.
    두 번째 줄에 N개의 숫자가 차례로 주어진다.
[OUTPUT]
각 케이스별 k번째 수를 아래 출력예제와 같이 출력하세요.

[INPUT EX]
2  -> 테스트 케이스 개수
6 2 5 3 -> 첫번째 테스트 케이스에 대한 N, s, e, k
5 2 7 3 8 9
15 3 10 3 -> 두번째 테스트 케이스에 대한 N, s, e, k
4 15 8 16 6 6 17 3 10 11 18 7 14 7 15

[OUTPUT EX]
#1 7
#2 6
"""

def solution(T):
    # test 개수만큼 받아들이기
    case, case_ = [],[]
    for i in range(T):
        case.append(map(int, input().split()))
        case_.append(list(map(int, input().split())))
    count = 1
    for c1, c2 in zip(case,case_):
        N, s, e, k = c1
        if N != len(c2): return -1
        c2 = c2[s-1:e+1]
        c2.sort()
        print("#"+str(count),c2[k-1])
        count += 1

if __name__ == "__main__":
    T = int(input())
    print(solution(T))