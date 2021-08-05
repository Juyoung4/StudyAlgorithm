# 가장 먼 노드
# https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque

def bfs(infos, n):
    keys = infos.keys()
    
    queue = deque()
    queue.append([1, 0])
    visitied = [-1 for i in range(n+1)]
    visitied[1] = 0
    
    max_value, max_count = -1, -1
    while queue:
        n, count = queue.popleft()
        for next_n in infos[n]:
            if visitied[next_n] == -1 or visitied[next_n] > count+1:
                visitied[next_n] = count+1
                queue.append([next_n, count+1])
                if max_value < count+1: max_value, max_count = count+1, 1
                elif max_value == count+1: max_count += 1
    return max_count

def solution(n, edge):
    answer = 0
    if n == 2: return 1
    infos = dict()
    for i in range(1, n+1):
        infos[i] = []
    for n1, n2 in edge:
        infos[n1].append(n2)
        infos[n2].append(n1)
    if not infos[1]: return answer
    
    answer = bfs(infos, n)
    
    return answer

print(solution(	6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))