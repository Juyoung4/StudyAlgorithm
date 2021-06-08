# 124나라의 숫자

def solution(n):
    answer = ''
    three = 0
    temp = 0
    while temp + 3**three <= n:
        temp += 3**three 
        three += 1
    # 자릿 수 : three / 시작 부터 몇 번째 수 : n-temp+1
    jump = n-temp+1
    temp = three-1
    for _ in range(three):
        threes = 3**temp
        if 1 <= jump <= threes: # 1 _ _
            answer += str(1)
        elif threes < jump <= threes*2:
            answer += str(2)
            jump -= threes
        else:
            answer += str(4)
            jump -= threes*2
        temp -= 1
    return answer

print(solution(27))

"""
def change124(n):
    num = ['1','2','4']
    answer = ""


    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(change124(10))
"""