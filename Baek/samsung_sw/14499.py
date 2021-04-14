# 주사위굴리기
# https://www.acmicpc.net/problem/14499

import sys

# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def grid_move(grids, x, y, moves, N, M):
    s = [0] * 6 # 위, 앞, 오른, 바닥, 뒤, 왼쪽
    cur_r, cur_c = x, y

    for i in range(len(moves)):
        next_r, next_c = cur_r + dirs[moves[i]][0], cur_c + dirs[moves[i]][1]
        if 0 <= next_r < N and 0 <= next_c < M:
            cur_r, cur_c = next_r, next_c
            if moves[i] == 0: # 동쪽이면 -> 위 = 왼, 왼 = 바닥, 바닥 = 오른, 오른 = 위
                t = s[0]
                s[0], s[5], s[3] = s[5], s[3], s[2]
                s[2] = t
            elif moves[i] == 1: # 서쪽 이면 위=오른, 오른=바닥, 바닥=왼, 왼=위
                t = s[0]
                s[0], s[2], s[3] = s[2], s[3], s[5]
                s[5] = t
            elif moves[i] == 2: # 북쪽이면 위 = 앞, 앞=바닥, 바닥= 뒤, 뒤 = 위
                t = s[0]
                s[0], s[1], s[3] = s[1], s[3], s[4]
                s[4] = t
            else: # 남쪽이면 위 = 뒤, 뒤 = 바닥, 바닥 = 앞, 앞 = 위
                t = s[0]
                s[0], s[4], s[3] = s[4], s[3], s[1]
                s[1] = t
            if not grids[next_r][next_c]: # gird에 쓰여 있는 수가 0이면 주사위 바닥면을 복사시킴
                grids[next_r][next_c] = s[3]
            else:
                s[3] = grids[next_r][next_c]
                grids[next_r][next_c] = 0
            #print(s, (next_r, next_c))
            print(s[0])
    return
            




if __name__ == "__main__":

    N, M, x, y, K = map(int, sys.stdin.readline().split())
    grids = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    moves = [num-1 for num in list(map(int ,sys.stdin.readline().split()))]
    grid_move(grids, x, y, moves, N, M)
    