# 숫자만 추출
"""
문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만듭니다.
만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.
만약 “t0e0a1c2h0er”에서 숫자만 추출하면 0, 0, 1, 2, 0이고 이것을 자연수를 만들면 120이
됩니다. 즉 첫 자리 0은 자연수화 할 때 무시합니다. 
출력은 120를 출력하고, 다음 줄에 120의 약수의 개수를 출력하면 됩니다.

[INPUT]
첫 줄에 숫자가 썩인 문자열이 주어집니다. 문자열의 길이는 50을 넘지 않습니다.

[OUTPUT]
첫 줄에 자연수를 출력하고, 두 번째 줄에 약수의 개수를 출력합니다.

[INPUT EX]
g0en2Ts8eSoft

[OUTPUT EX]
28
6
"""

def solution(st):
    result = ""
    for s in st:
        if s.isdigit() and (((result == "") and s != "0") or (result != "")):
            result += s
    result = int(result)
    # 약수 개수 구하기
    count = 0
    for i in range(1, int(result**0.5)+1):
        if not result % i: count += 1
    return (result, count*2)

    
if __name__ == "__main__":
    print(solution(input()))