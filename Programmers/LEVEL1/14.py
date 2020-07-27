# 문자열 내 p와 y의 개수
"""
문자열 함수 lower사용
"""
def solution(s):
    return True if s.lower().count("p") == s.lower().count("y") else False

