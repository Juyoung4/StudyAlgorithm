# 회문 문자열 검사

"""
N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열)이면
YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성

[INPUT]
첫 줄에 정수 N(1<=N<=20)이 주어지고, 그 다음 줄부터 N개의 단어가 입력
각 단어의 길이는 100을 넘지 않는다.

[OUTPUT]
각 줄에 해당 문자열의 결과를 YES 또는 NO로 출력한다.

[INPUT EX]
5
level
moon
abcba
soon
gooG

[OUTPUT EX]
#1 YES
#2 NO
#3 YES
#4 NO
#5 YES
"""

def solution(N):
    result = []
    for i in range(N):
        s = input().lower()
        len_ = len(s)
        if len_ % 2: # 홀수
            if s[:len_//2] == s[len_//2+1:][::-1]:
                result.append(True)
            else:
                result.append(False)
        else:
            if s[:len_//2] == s[len_//2:][::-1]:
                result.append(True)
            else:
                result.append(False)
    return result

def solution2(N):
    result = []
    for i in range(N):
        s = input().lower()
        if s == s[::-1]:
            result.append(True)
        else:
            result.append(False)
    return result
    
if __name__ == "__main__":
    print(solution(int(input())))