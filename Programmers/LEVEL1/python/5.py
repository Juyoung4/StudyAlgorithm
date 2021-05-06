# 짝수와 홀수
def solution(num):
    if type(num) == float: return
    return "Even" if num % 2 == 0 else "Odd"

# 다른 사람 풀이
def evenOrOdd(num):
    return ["Even", "Odd"][num & 1]
## 풀이: 2진 비트에서 1번째 자리가 0이면 짝, 1이면 홀이니까...개 천재
## 비트 연산을 자주 이용해서 풀면 좋음!
