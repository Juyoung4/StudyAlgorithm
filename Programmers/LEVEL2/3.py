# 기능 개발
def solution(progresses, speeds):
    # 기능 100 -> 서비스 반영
    # 뒤에 기능이 먼저 개발 가능 but 앞에 기능이 배포될때 함께 배포
    # progresses: 작업의 진도
    # speeds: 작업의 개발 속도
    if len(progresses) >= 100 and len(speeds) > 100: return False
    
    day = []
    pre, count = 0,0
    for idx,value in enumerate(zip(progresses, speeds)):
        temp = (100-value[0])//value[1] if not (100-value[0])%value[1] else (100-value[0])//value[1]+1
        if not idx: pre = temp
        else:
            if pre < 
    
    
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))