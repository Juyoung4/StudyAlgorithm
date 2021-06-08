# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    len_s = len(s)
    answer = len_s
    for i in range(1, len_s//2+1):
        result = 0
        t = ""
        temp, cnt = "", 0
        for j in range(0, len_s, i):
            check = s[j:j+i]
            if not temp:
                temp = check
                cnt += 1
            elif temp == check:
                cnt += 1
                if j+i == len_s:
                    t += temp+str(cnt) if cnt > 1 else temp
                    result += i+len(str(cnt)) if cnt > 1 else i
            elif temp != check:
                t += temp+str(cnt) if cnt > 1 else temp
                result += i+len(str(cnt)) if cnt > 1 else i
                temp = check
                cnt = 1
                if j+i == len_s:
                    t += temp+str(cnt) if cnt > 1 else temp
                    result += i+len(str(cnt)) if cnt > 1 else i
        if i != 1 and len_s%i != 0:
            result += len(s[j:])
        
        answer = min(answer, result)
    return answer