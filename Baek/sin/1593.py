# https://www.acmicpc.net/problem/1593
# 문자 해독

if __name__ == "__main__":
    w_l, s_l = map(int, input().split())
    W = input()
    S = input()
    if w_l == 1: print(S.count(W))
    else:
        answer = 0
        # ord('a') => 97 , ord('A') => 65
        # a-z => 97~122 / A-Z => 65~90
        alpha = [0]*52 # A-Z : 0 ~ 25 / a-z : 26 ~ 51
        for s in W:
            n = ord(s)
            if n <= 90: alpha[n-65] += 1
            else: alpha[n-71] += 1
        
        temp = [0]*52
        for i in range(s_l):
            s = ord(S[i])
            if s <= 90: temp[s-65] += 1
            else: temp[s-71] += 1
            
            if i+1 >= w_l:
                if temp == alpha: answer += 1

                pre = ord(S[i+1-w_l])
                if pre <= 90: temp[pre-65] -= 1
                else: temp[pre-71] -= 1
        print(answer)

"""
W = 특정 단어 => 각 글자가 뭔지는 아는데 이것이 고대 기록에 어떤 형태로 숨어 있는지 X
W = g개 그림 문자
마야 문자열 = S
단어 W가 S에 들어있는 모든 가짓 수
 문자열  S안에서 문자열 W의 순열 중 하나가 
 부분 문자열로 들어있는 모든 경우의 수를 계산하라는 뜻이다.

즉, W로 순열을 만듬 => 그리고 그 모든 순열이 S안에 있는지 확인
"""