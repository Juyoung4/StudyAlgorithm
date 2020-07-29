#시저 암호
"""
ASCII코드 -> STRING: chr()
STRING -> ASCII코드: ord()
"""


def solution(s, n):
    answer=""
    up='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low='abcdefghijklmnopqrstuvwxyz'
    for i in s:
        if ord(i) in range(65,91): #대문자
            idu=up.find(i)+n
            print(idu)
            if idu > 25:
                answer += up[idu-26]
            else:
                answer += up[idu]
        elif ord(i) in range(97,123):
            idu=low.find(i)+n
            print(idu)
            if idu > 25:
                answer += low[idu-26]
            else:
                answer += low[idu]
        else:
            answer += " "
    return answer

print(solution("z",1))

# 다른사람 풀이
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)

# isupper와 islower함수를 사용해서 대문자 소문자 파악