# 기능 개발
def solution(progresses, speeds):
    result, temp = [], 0
    for i in range(len(progresses)):
        p = (100-progresses[i])//speeds[i]
        if (100-progresses[i])%speeds[i] > 0: p += 1
        if i == 0:
            temp = p
            result.append(1)
            continue
        if p > temp:
            result.append(1)
            temp= p
        else:
            result[-1] += 1
    return result
        
# 다른 사람 풀이
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
    
print(
    solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
)