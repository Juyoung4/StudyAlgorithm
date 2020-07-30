#2018 KAKAO BLIND RECRUITMENT [1차] 다트 게임
"""
문자 바꾸기는 maketrans와 translate함수를 이용하면 편함
"""
def solution(dartResult):
    # 다트 3번 던져 점수 함계
    # 점수: 0~10점 + 영역 Single, Double, Triple
    # 옵션: *(해당 점수*2 + 직전 점수*2) , #(직전 점수 - 해당 점수)
            # *은 첫번째 시작하자마자 가능: 첫번째 점수*2
            # **이 나오면 점수는 4배
            # *# 나오면 점수는 -2배
    pre,cru,result=0,0,0 #pre는 이전 결과 값?, cru는 현재 결과값?
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if not int(dartResult[i]) and cru==1:
                cru=10
            else:
                cru=int(dartResult[i])
        else:
            if dartResult[i]=="S":
                if i+1 < len(dartResult) and dartResult[i+1]=="#":
                    result += cru*-1
                    pre = cru*-1
                    continue
                if i+1 < len(dartResult) and dartResult[i+1]=="*":
                    if i == 2:
                        result += cru*2
                        pre = cru*2
                        continue
                    else:
                        result -= pre
                        result += (pre*2+cru*2)
                        pre = cru*2
                        continue
                else:
                    result += cru
                    pre = cru
                    continue
            if dartResult[i]=="D":
                if i+1 < len(dartResult) and dartResult[i+1]=="#":
                    result += cru**2*-1
                    pre = cru**2*-1
                    continue
                if i+1 < len(dartResult) and dartResult[i+1]=="*":
                    if i == 2:
                        result += cru**2*2
                        pre = cru**2*2
                        continue
                    else:
                        result -= pre
                        result += (pre*2+cru**2*2)
                        pre = cru**2*2
                        continue
                else:
                    result += cru**2
                    pre = cru**2
                    continue
            if dartResult[i]=="T":
                if i+1 < len(dartResult) and dartResult[i+1]=="#":
                    result += cru**3*-1
                    pre = cru**3*-1
                    continue
                if i+1 < len(dartResult) and dartResult[i+1]=="*":
                    if i == 2:
                        result += cru**3*2
                        pre = cru**3*2
                        continue
                    else:
                        result -= pre
                        result += (pre*2+cru**3*2)
                        pre = cru**3*2
                        continue
                else:
                    result += cru**3
                    pre = cru**3
                    continue
            
    return result

        
print(solution("1S2D*3T"))


# 정규식 풀이
"""
정규식 사용법 공부해야함
"""
import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

    