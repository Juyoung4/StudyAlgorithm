# 괄호 검사

"""
영어 소문자와 '[' ']'로만 이루어진 문자열이 주어졌을 때, 
짝이 맞지 않는 '[' 또는 ']'가 존재한다면 False를, 
존재하지 않는다면 True를 출력하는 프로그램 작성

[입력]
8
he[ll]o]

[출력]
False
"""

def solution(N):
    stack = list()
    s = input()
    for i in s:
        if i.isalnum(): continue
        if i == '[':
            stack.append(i)
            continue
        if i == ']' and stack:
            stack.pop()
        else:
            return False
    return False if stack else True
    
if __name__ == "__main__":
    print(solution(int(input())))