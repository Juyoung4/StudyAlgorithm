# 수박수박수박수박수박수?
def solution(n):
    if n < 0 and n > 10000: return
    return "".join(["수" if i%2==0 else "박" for i in range(n)])

# 다른 사람 풀이
def solution(n):
    s = "수박" * n
    return s[:n]

# 리스트 -> 메모리 소비량 너무 많아서 사용 안하는게 좋음
# 문자열만 가지고 하면 메모리 소비량 적고 계산량 적음
# 문자열 가지고 푸는 공부 하기@
