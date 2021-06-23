# jadenCase 문자열 만들기
def solution(s):
    s = s.lower()
    s = s.split(" ")
    print(s)
    answer = ""
    for st in s:
        if st == "": answer += " "
        else: answer += (st[0].upper()+st[1:]+" ")
        
    return answer[:-1]

print(solution("  a2312 3asPe P123sxz"))
