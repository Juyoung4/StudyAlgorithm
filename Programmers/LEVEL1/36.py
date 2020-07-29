#[1차]비밀지도
"""
2진수: 0b
8진수: 0o
16진수: 0x

bin(), oct(), hex()라는 내장 함수: 10진수를 각각의 진수로 바꿔줌(스트링으로)
"""
def solution(n, arr1, arr2):
    answer=[]
    m=[arr1[i] | arr2[i] for i in range(n)]
    for i in m:
        if len(bin(i)[2:]) < n:
            i="0"*(n-len(bin(i)[2:]))+bin(i)[2:]
        else:
            i=bin(i)[2:]
        answer.append(i.replace("0"," ").replace("1","#"))
    return answer
            
def solution(n, arr1, arr2):
    m=[arr1[i] | arr2[i] for i in range(n)]
    return [("0"*(n-len(bin(i)[2:]))+bin(i)[2:]).replace("0"," ").replace("1","#") if len(bin(i)[2:]) < n else bin(i)[2:].replace("0"," ").replace("1","#") for i in m]

#위 아래 같은 코드 -> 위 코드를 아래 처럼 한줄로 작성ㅇ해봄