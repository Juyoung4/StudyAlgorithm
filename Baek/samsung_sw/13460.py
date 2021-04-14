# 구슬탈출2
import sys
from collections import deque

def BFS(red_r, red_c, hole_r, hole_c, blue_r, blue_c, grids):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)] # 4차원 배열
    visited[blue_r][blue_c][red_r][red_c] = True
    queue = deque()
    queue.append((red_r, red_c, blue_r, blue_c, 1))

    while queue:
        red_r, red_c, blue_r, blue_c, moves = queue.popleft()

        if moves > 10:
            return -1

        for dir_r, dir_c in dirs:
            # 두개 공 움직임
            next_blue_r, next_blue_c, b_move_count = move(blue_r, blue_c, dir_r, dir_c)
            next_red_r, next_red_c, r_move_count = move(red_r, red_c, dir_r, dir_c)

            if grids[next_blue_r][next_blue_c] == 'O': # 파란 공이 먼저 hole에 빠짐
                continue # 이 방법 사용하면 x
            if grids[next_red_r][next_red_c] == 'O':
                return moves
            
            if next_red_r == next_blue_r and next_red_c == next_blue_c: # 같은 칸에 있을 수 없기 때문에 하나가 이동해야함
                if r_move_count > b_move_count: # 이동 거리가 많은 구슬이 한칸 뒤로 가는게 맞음
                    next_red_r -= dir_r
                    next_red_c -= dir_c
                else:
                    next_blue_r -= dir_r
                    next_blue_c -= dir_c
            
            # visited에 기록해야함 들린적 없으면 해당 구슬 정보 입력
            if not visited[next_blue_r][next_blue_c][next_red_r][next_red_c]: # 들린적 없으면
                visited[next_blue_r][next_blue_c][next_red_r][next_red_c] = True
                queue.append((next_red_r, next_red_c, next_blue_r, next_blue_c, moves + 1))
    return -1

def move(r, c , dir_r, dir_c):
    move_count = 0
    while grids[r+dir_r][c+dir_c] != '#' and grids[r][c] != 'O':
        move_count += 1
        r += dir_r
        c += dir_c
    return r, c, move_count
        
if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    red_r, red_c = 0, 0
    blue_r, blue_c = 0, 0
    hole_r, hole_c = 0, 0

    grids = []

    for i in range(N):
        temp = sys.stdin.readline().strip()
        temp2 = []
        for j in range(M):
            temp2.append(temp[j])
            if temp[j] == 'B':
                blue_r, blue_c = i, j
                temp2[j] = '.'
                continue
            if temp[j] == 'R':
                red_r, red_c = i, j
                temp2[j] = '.'
                continue
            if temp[j] == 'O':
                hole_r, hole_c = i, j
                continue
        grids.append(temp2)

    print(BFS(red_r, red_c, hole_r, hole_c, blue_r, blue_c, grids))