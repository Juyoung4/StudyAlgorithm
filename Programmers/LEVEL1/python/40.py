#2019 KAKAO BLIND RECRUITMENT 실패율

import collections
def solution(N, stages):
    status,result,p=collections.Counter(stages),[],0
    
    for i in range(N):
        if i+1 in status.keys(): 
            if not i: 
                result.append((i+1, status[i+1]/len(stages)))
                p += status[i+1]
                continue
            else:
                result.append((i+1, status[i+1]/(len(stages)-p)))
                p+=status[i+1]
                continue
        else:
            result.append((i+1,0))
            continue
        if i+1==N and N+1 in status.keys():
            result.append((i+1,status[N+1]/len(stages)-p))
            continue
    return [i[0] for i in sorted(result,key=lambda x: (-x[1], x[0]))]
    

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))