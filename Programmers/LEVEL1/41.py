# 신규아이디 추천
import re
def solution(new_id):
    answer = ''
    # 1단계 : 대문-> 소문
    new_id = new_id.lower()
    # 2단계 : 소문자, 숫자, -, _, .
    new_id = re.sub('[^a-z0-9._-]', '', new_id)  
    # 3단계 : . 2번 이상 -> 하나의 마침표
    if len(new_id) >= 1:
        pre = new_id[0]
        answer = pre
        for s in new_id[1:]:
            if pre == '.' and s == '.': pass
            else: answer += s
            pre = s
    # 4단계 : . 처음 끝 에 있응면 제거
    if len(answer) >= 1 and answer[0] == '.': answer = answer[1:]
    if len(answer) >= 1 and answer[-1] == '.': answer = answer[:-1]
    # 5단계 ; 
    if not answer: answer = 'a'
    # 6단계
    if len(answer) >= 16: answer = answer[:15]
    if len(answer) > 1 and answer[-1] == '.': answer = answer[:-1]
    # 7단계
    len_ = len(answer)
    if len_ <= 2:
        t = answer[-1]
        for i in range(3-len_):
            answer += t
    return answer


"""
입력된 아이디와 유사하면서 규칙에 맞는 아이디 추천
아이디 : 소문자, 숫자, -, _, . 만 사용 (.는 처음과 끝 사용 x 연속 x)

"""