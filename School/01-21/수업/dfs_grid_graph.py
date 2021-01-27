N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

start = (0, 0)
result = 0
def inRange(x, y):
    return 0 <= x < N and 0 <= y < M

def check(x, y):
    if not inRange(x, y): return False
    if visited[x][y] or grid[x][y] == 0: return False
    else:
        return True
    
def DFS(x, y):
    # direction
    dx = (1, 0)
    dy = (0, 1)
    
    for i in range(2):
        next_x, next_y = x + dx[i], y + dy[i]
        if check(next_x, next_y):
            visited[next_x][next_y] = 1
            DFS(next_x, next_y)
visited[0][0] = 1
DFS(start[0], start[1])
print(visited[N-1][M-1])

