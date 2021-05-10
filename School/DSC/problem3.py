# 징검다리

"""
민석이는 첫번째 돌을 밟고 서 있고 정확히 마지막돌에 도착하려고 한다.
징검다리의 돌 위에는 음이 아닌 정수가 쓰여 있고 밟고 있는 돌에 적힌 숫자만큼 최대 이동 가능.
(ex)
2 4 1 2 5 7 일 때, 첫번째 돌에서 두번째 돌로 한번 건너가고 두번째 돌에서 마지막 돌까지 네번 건너가면
마지막 돌에 도착 가능 => True

[입력]
5
3 2 1 0 4

[출력]
False
"""

def solution(n, stones):
    if n != len(stones): return -1
    return False if 0 in stones else True
    
if __name__ == "__main__":
    print(solution(int(input()), list(map(int, input().split()))))