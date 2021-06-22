# 소수찾기
result = []
def per(numbers, k, cur_string, visited):
    if len(cur_string) == k:
        temp = int(cur_string)
        if temp not in result and cur_string[0] != '0':
            result.append(temp)
        return
    for i in range(len(numbers)):
        if not visited[i]:
            visited[i] = 1
            per(numbers, k, cur_string+numbers[i], visited)
            visited[i] = 0
    return

def solution(numbers):
    answer = 0
    
    length = len(numbers)
    
    for i in range(1, length+1):
        per(numbers, i, "", [0]*length)
    
    max_ = max(result)+1
    temp = [1, 1] + [0]*(max_-1)
    sqrt = int(max_**(0.5))+1
    for i in range(2, sqrt):
        if not temp[i]:
            for j in range(i+i, max_, i):
                temp[j] = 1
    
    for r in result:
        if not temp[r]:
            answer += 1
    
    return answer