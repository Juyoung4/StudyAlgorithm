# 조이스틱
def solution(name):
    answer = 0

    result = "A"*len(name)
    print(result)

    # 1. 차이를 계산하기
    diff = []
    for n in name:
        o = ord(n)
        if o >= 78:
            diff.append(91-o)
        else:
            diff.append(o-65)
    
    print(diff)

    return answer


print(solution("JANOCAP")) # JEROEN
"""
1. 다음 알파벳
2. 이전 알파벳(A면 Z로)
3. +1 문자로 넘어감 (맨뒤면 맨 앞)
4. -1 문자로 넘어감 (첫번째면 맨뒤로)

참고 A~N인 경우는 <-으로 건너띄고, O~Z는 -> 방향으로 건너띄어야 짧다.
N = 78임



"""