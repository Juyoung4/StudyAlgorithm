# 가운데 글자 가져오기
def solution(s):
    l=len(s)
    return s[l//2-1:l//2+1] if l % 2 == 0 else s[l//2]

# 한줄로 l대신 len(s)쓰면 조금 더 오래 걸리니 이렇게 푸는게 더 빠름!

