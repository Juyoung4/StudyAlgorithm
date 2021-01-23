n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(n)]
hospital = [] # 병원 위치
people = [] # 사람 위치
for i in range(n):
    for j in range(n):
        if roads[i][j] == 2:
            hospital.append((i,j))
            continue
        if roads[i][j] == 1:
            people.append((i,j))
visited = [0 for _ in range(len(hospital))]

import sys
INT_MAX = sys.maxsize
min_ = INT_MAX

def find_min(combi):
    global min_
    result = 0
    # 각 사람마다 병원에서 가장 가까운 거리 탐색
    for p in people:
        p_min = INT_MAX
        for h in combi:
            p_min = min(p_min, ((abs(h[0] - p[0]) + abs(h[1] - p[1]))))
        result += p_min
    min_ = min(min_, result)           
    return
                            
def find_combi(cur_num, last_num):
    if cur_num == m:
        temp = []
        for i in range(len(hospital)):
            if visited[i]:
                temp.append(hospital[i])
        #print(temp)
        find_min(temp)
        #print(min_)
        return

    for i in range(last_num+1, len(hospital)):
        visited[i] = 1
        find_combi(cur_num+1, i)
        visited[i] = 0

# 나올 수 있는 순열 조합
for i in range(len(hospital)):
    visited[i] = 1
    find_combi(1, i)
    visited[i] = 0

print(min_)