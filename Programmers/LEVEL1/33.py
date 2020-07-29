#모의고사
answer = [[1,0],[[2,1],0],[[3,0],0]]
step = [1,3,4,5]
step2 = [3,1,2,4,5]
def solution(answers):
    global answer
    global step
    global step2
    result=[]
    for i in answers:
        if answer[0][0] == i:
            answer[0][1] += 1
        if answer[1][0][0] == i:
            answer[1][1] += 1
        if answer[2][0][0] == i:
            answer[2][1] += 1

        answer[0][0] = (answer[0][0]+1)%5 if answer[0][0]+1 > 5 else answer[0][0]+1

        if answer[1][0][0] == 2:
            answer[1][0][0] = answer[1][0][1]
            answer[1][0][1] = 2
        else:
            answer[1][0][1] = step[(step.index(answer[1][0][0])+1)%4]
            answer[1][0][0] = 2
        
        if not answer[2][0][1]:
            answer[2][0][1] += 1
        else:
            answer[2][0][1] = 0
            answer[2][0][0] = step2[(step2.index(answer[2][0][0])+1)%5]
    
    answer=[i[1] for i in answer]
    answer=answer+[max(answer)]
    for i in range(len(answer)-1):
        if answer[i] == answer[-1]:
            result.append(i+1)
    return result

#문제를 잘못알아땨...