# 문자열 내림차순으로 배치하기
# 조건 : str은 길이 1이상인 문자열
def solution(s):
    if str < 1: return
    answer=""
    for i in sorted(s, reverse=True):
        answer += i
    return answer

# 다른 사람 답
def solution(s):
    if str < 1: return
    return ''.join(sorted(s, reverse=True))

"""
📃 문자열 함수 join과 split를 잘 활용하기!!!
"""