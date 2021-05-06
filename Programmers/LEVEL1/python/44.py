# 44. 월간 코드 챌린지 시즌2 음양 더하기
def solution(absolutes, signs):
    answer = 0
    for num, s in zip(absolutes, signs):
        if s: answer += num
        else: answer += -num
    return answer

"""
정수들의 절댓값 = absolutes / 정수 부호 = signs
"""