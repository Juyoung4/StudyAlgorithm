#테트로미노 https://www.acmicpc.net/problem/14500
import sys

# version 1 : 시뮬 -> 시간 너무 오래 걸림
"""
if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    grids = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    dirs = [
        [(0, 1), (0, 2), (0, 3)], # 1-1. 한줄 - 가로
        [(1, 0), (2, 0), (3, 0)], # 1-2. 한줄 - 세로
        [(0, 1), (1, 0), (1, 1)], # 2. ㅁ자
        [(0, 1), (1, 1), (2, 1)], # 3-1. ㄴ자 세로 - 1
        [(0, -1), (1, -1), (2, -1)], # 3-2. ㄴ자 세로 - 2
        [(0, 1), (-1, 1), (-2, 1)], # 3-3. ㄴ자 세로 - 3
        [(0, -1), (-1, -1), (-2, -1)], # 3-4.ㄴ자 세로 - 4
        [(1, 0), (1, 1), (1, 2)], # 3-5. ㄴ자 가로 - 1
        [(1, 0), (1, -1), (1, -2)], # 3-6. ㄴ자 가로 - 2
        [(-1, 0), (-1, 1), (-1, 2)] , # 3-7. ㄴ자 가로 - 3
        [(-1, 0), (-1, -1), (-1, -2)], # 3-8. ㄴ자 가로 - 4
        [(1, 0), (1, -1), (1, 1)], # 4-1. ㅗ
        [(-1, 0), (-1, -1), (-1, 1)], # 4-2. ㅜ
        [(0, 1), (-1, 1), (1, 1)], # 4-3. ㅓ
        [(0, -1), (-1, -1), (1, -1)], # 4-4. ㅏ
        [(1, 0), (1, 1), (2, 1)], # 5-1. ㄹ 위
        [(1, 0), (1, -1), (2, -1)], # 5-2. ㄹ 위 대칭
        [(0, 1), (1, 1), (1, 2)], # 5-3. ㄹ 가로
        [(0, -1), (1, -1), (1, -2)] # 5-4. ㄹ 대칭
    ]

    max_ = 0
    for i in range(N):
        for j in range(M):
            for d in dirs:
                temp = grids[i][j]
                for r, c in d:
                    next_r, next_c = i+r, j+c
                    if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M: break
                    temp += grids[next_r][next_c]
                else:
                    max_ = max(temp, max_)
                    #print("check : ", (i, j), d, max_)
    
    print(max_)
"""

max_ = 0
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def DFS(visited, r, c, length, sums):
    global max_
    if length == 3:
        max_ = max(max_, sums)
        return
    
    for i, j in dirs:
        next_r, next_c = r+i, c+j
        if 0 <= next_r < N and 0 <= next_c < M and not visited[next_r][next_c]:
            visited[next_r][next_c] = True
            DFS(visited, next_r, next_c, length+1, sums+grids[next_r][next_c])
            visited[next_r][next_c] = False

    

# version2 : DFS이용 + ㅗ는 DFS 사용 X 
if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    grids = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    dirs_temp = [
        [(1, 0), (1, -1), (1, 1)], # 4-1. ㅗ
        [(-1, 0), (-1, -1), (-1, 1)], # 4-2. ㅜ
        [(0, 1), (-1, 1), (1, 1)], # 4-3. ㅓ
        [(0, -1), (-1, -1), (1, -1)] # 4-4. ㅏ
    ]
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            # dfs
            visited[i][j] = True
            DFS(visited, i, j, 0, grids[i][j])
            visited[i][j] = False

            # ㅗ 순회
            for d in dirs_temp:
                temp = grids[i][j]
                for r, c in d:
                    next_r, next_c = i+r, j+c
                    if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M: break
                    temp += grids[next_r][next_c]
                else:
                    max_ = max(temp, max_)
    
    print(max_)

