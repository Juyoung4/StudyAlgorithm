#이상한 문자 만들기

def solution(s):
    answer=""
    s=s.split(" ")
    for i in s:
        for j in range(len(i)//2+1):
            if 2*j < len(i):
                answer += i[2*j].upper()
            if 2*j + 1 < len(i):
                answer += i[2*j+1].lower()
        answer += " "
    return answer[:-1]

#다른 사람 풀이
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

#열거형으로 풀었뜨..대박