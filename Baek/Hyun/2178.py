# 미로 탐색

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

from collections import deque
def bfs(N, M, visited):
    queue = deque()
    queue.append([0, 0, 1])
   
    while queue:
        r, c, count = queue.popleft()
        if r == N-1 and c == M-1:
            break
        for i,j in dirs:
            next_r, next_c = r+i, c+j

            if 0 <= next_r < N and 0 <= next_c < M and not visited[next_r][next_c] and grids[next_r][next_c] == '1':
                visited[next_r][next_c] = 1
                queue.append([next_r, next_c, count+1])
    return count

min_ = 10000
def dfs(N, M, r, c, count, visited):
    global min_
    if r == N-1 and c == M-1:
        min_ = min(min_, count)
        return count
    
    for i, j in dirs:
        next_r, next_c = r+i, c+j
        if 0 <= next_r < N and 0 <= next_c < M and not visited[next_r][next_c] and grids[next_r][next_c] == '1':
            visited[next_r][next_c] = 1
            dfs(N, M, next_r, next_c, count+1, visited)
            visited[next_r][next_c] = 0
            

if __name__ == "__main__":
    N, M = map(int, input().split())
    N, M = N, M

    grids = [input() for _ in range(N)]

    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    #print(bfs(N, M, visited))

    dfs(N, M, 0, 0, 1, visited)
    print(min_)
    