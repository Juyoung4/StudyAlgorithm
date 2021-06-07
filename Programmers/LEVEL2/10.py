# 주식 가격
def solution(prices):
    len_p = len(prices)
    answer = [0]*len_p
    stack = []
    
    for time, p in enumerate(prices):
        if time == len_p-1:
            while stack:
                temp_time, temp_p = stack.pop()
                answer[temp_time] = time - temp_time
            break
        if not stack: 
            stack.append([time, p])
        else:
            if stack[-1][1] <= p: # stack안에 주식 가격 <= 현재 주식 가격 => 가격 상승 or 유지
                stack.append([time, p])
            else:
                while stack:
                    if stack[-1][1] > p:
                        temp_time, temp_p = stack.pop()
                        answer[temp_time] = time - temp_time
                    else:
                        break
                stack.append([time, p]) 
            
    return answer
    
print(solution([1,2,3,2,3]))