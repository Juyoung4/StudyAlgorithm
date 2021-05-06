# 48. 월간 코드 챌린지 시즌1 두 개 뽑아서 더하기
answer = []
def combi(count, last_num, visited, len_a, numbers):
    global answer
    if count == 2:
        temp = 0
        for i in range(len_a):
            if visited[i]: temp += numbers[i]
        if temp not in answer: answer.append(temp)
        return
    
    for i in range(last_num, len_a):
        if not visited[i]:
            visited[i] = True
            combi(count+1, i+1, visited, len_a, numbers)
            visited[i] = False

def solution(numbers):
    len_a = len(numbers)
    combi(0, 0, [0]*len_a, len_a, numbers)
    answer.sort()
    return answer

"""
서로 다른 인덱스에 있는 두개의 수를 뽑아 더해 만들 수 있는 모든 수 => 오름차순
"""
"""

"""