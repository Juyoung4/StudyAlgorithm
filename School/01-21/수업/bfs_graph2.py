from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

queue = deque([])

def inRange(x, y):
    return 0 <= x < N and 0 <= y < M

def check(x, y):
    if not inRange(x,y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def push(x, y, d):
    queue.append((x, y))
    visited[x][y] = d

def BFS():
    # direction -상 하 좌 우
    dx = (-1, 1, 0 , 0)
    dy = (0, 0, 1, -1)
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x, next_y = x + dx[i], y + dy[i]
            if check(next_x, next_y):
                push(next_x, next_y, visited[x][y]+1)
                
push(0, 0, 0)
BFS()
print(visited[N-1][M-1] if visited[N-1][M-1] else -1)