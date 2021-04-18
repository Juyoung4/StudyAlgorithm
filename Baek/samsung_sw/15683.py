#감시 https://www.acmicpc.net/problem/15683

import sys
from collections import defaultdict

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dfs(cnt):
    global visited, total
    if cnt == cctv_num:
        temp = [i[:] for i in grids]
        temp_count = 0
        #print("cctvs : ", cctvs, ", visited :", visited)
        for i in range(cctv_num):
            r, c = cctvs[i][0], cctvs[i][1]
            #print("basic : ",(r, c), (dirs[visited[i]][0], dirs[visited[i]][1]))
            t, temp = spread(temp, dirs[visited[i]][0], dirs[visited[i]][1], r, c) # 1, 2, 3, 4 모두 수행
            temp_count += t
            if temp[r][c] == 2 or temp[r][c] == 4:
                #print("2 or 4 : ",(r, c), (dirs[(visited[i]+2)%4][0], dirs[(visited[i]+2)%4][1]))
                t, temp =  spread(temp, dirs[(visited[i]+2)%4][0], dirs[(visited[i]+2)%4][1], r, c) # 마주보는 방향
                temp_count += t
            if temp[r][c] == 3 or temp[r][c] == 4:
                #print("3 or 4 : ",(r, c), (dirs[(visited[i]+1)%4][0], dirs[(visited[i]+1)%4][1]))
                t, temp =  spread(temp, dirs[(visited[i]+1)%4][0], dirs[(visited[i]+1)%4][1], r, c) # 바로 옆 방향
                temp_count += t
        
        total = min(total, checks-temp_count)
        return

    for i in range(4):
        visited[cnt] = i
        dfs(cnt+1)
        visited[cnt] = -1

def spread(g_temp, x, y, cur_r, cur_c):
    cur_r += x
    cur_c += y
    t = 0
    while 0 <= cur_r < N and 0 <= cur_c < M:
        if g_temp[cur_r][cur_c] == 6: return t, g_temp
        if g_temp[cur_r][cur_c] == 0: 
            g_temp[cur_r][cur_c] = '#'
            t += 1
        cur_r += x
        cur_c += y

    return t, g_temp

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    grids = []
    cctvs, cctv5 = [], []
    total = 0
    for i in range(N):
        temp = list(map(int, sys.stdin.readline().split()))
        grids.append(temp)
        for j in range(M):
            if temp[j] == 0: total += 1
            elif temp[j] == 5: cctv5.append((i, j))
            elif temp[j] in (1, 2, 3, 4): 
                cctvs.append((i, j))
    
    # 가장 먼저 5 처리 -> 방향 x
    for r, c in cctv5:
        for x, y in dirs:
            result, grids = spread(grids, x, y, r, c)
            total -= result

    checks = total
    # cctv 1 ~ 4 까지 dfs를 돌려 방향을 찾아준다
    cctv_num = len(cctvs)
    visited = [-1]*cctv_num
    dfs(0)

    print(total)
    
