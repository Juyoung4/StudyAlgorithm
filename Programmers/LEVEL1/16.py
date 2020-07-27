#문자열 다루기 기본
"""
isalpha함수는 문자열이 문자인지 아닌지를 True,False
isdigit함수는 문자열이 숫자인지 아닌지를 True,False
"""

def solution(s):
    return True if len(s) in (4,6) and s.isdigit() else False

# 다른 사람 코드
def alpha_string46(s):
    import re
    return bool(re.match("^(\d{4}|\d{6})$", s))

"""
정규식 re
메타 문자: . ^ $ * + ? { } [ ] \ | ( )

[https://wikidocs.net/4308] 공부하기
"""