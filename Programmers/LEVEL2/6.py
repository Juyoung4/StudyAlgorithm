from itertools import permutations

def init(expression):
    temp, new, c = '', [], set()
    l = {'-' : [], '+': [], '*': []}
    for s in expression:
        if s not in ('-+*'):
            temp += s
        else:
            new.append(int(temp))
            new.append(s)
            c.add(s)
            temp = ''
    return new+[int(temp)], c, l

def cal(temp_ex, order):
    total = 0
    print(temp_ex, order)
    for od in order:
        temp, len_temp = [], len(temp_ex)
        idx = 0
        while idx < len_temp:
            if temp_ex[idx] != od: # 해당 연산이 아니면
                temp.append(temp_ex[idx])
            else: # 해당 연산이면
                a = temp.pop()#이전 값 temp에 저장되어 있으니 빼기
                b = temp_ex[idx+1] # 다음 값임
                if od == '+': temp.append(a+b)
                elif od == '-': temp.append(a-b)
                else: temp.append(a*b)
                idx += 1
            idx += 1
        # 다 돌면 expression update
        temp_ex = temp[:]
    if temp_ex: return abs(temp_ex[0])
    else: return 0

def solution(expression):
    answer = 0
    expression, c, l = init(expression) # 수식 숫자, 연산 나누기
    orders = list(permutations(list(c), len(c)))

    for order in orders:
        answer = max(answer, cal(expression, order))
    return answer

print(solution("100-200*300-500+20"))
"""
연산 : + - *
연산자의 우선순위 자유롭게 재정의 만들어 가장 큰 숫자 제출
조건 : 같은 순위의 연산자 x [무조건 + > - > *] 이런식
조합

결과 = 음수면 절댓 값 제출
즉, 음수 개 작거나 양수 개 크거나
"""