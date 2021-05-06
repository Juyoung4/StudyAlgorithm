#체육복
#1은 빌려줌, 0은 빌려야함, 2는 못빌려줌
"""
그리드 알고리즘: 가장 현재 상태에서 최적의해를 선택
"""
def solution(n, lost, reserve):
    status=[0 if i in lost else 2 for i in range(n+1)]
    for i in reserve:
        if status[i]:
            status[i] = 1
        else:
            status[i] = 2
            lost.remove(i)
    for i in lost:
        if i==1:
            if status[i+1] == 1:
                status[i],status[i+1]=2,2
                continue
        elif i==n:
            if status[i-1] == 1:
                status[i-1],status[i]=2,2
                continue
        else:
            if status[i-1]==1 or status[i+1]==1:
                if status[i-1] == 1:
                    status[i-1],status[i]=2,2
                    continue
                if status[i+1] == 1:
                    status[i],status[i+1]=2,2
                    continue
    return n-status.count(0)

print(solution(3,[3],[1]))