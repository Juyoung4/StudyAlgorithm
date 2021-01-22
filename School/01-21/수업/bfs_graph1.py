from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

queue = deque([])

def inRange(x, y):
    return 0 <= x < N and 0 <= y < M

def check(x, y):
    return inRange(x,y) and not visited[x][y] and grid[x][y]
    
def BFS():
    # direction -상 하 좌 우
    dx = (-1, 1, 0 , 0)
    dy = (0, 0, 1, -1)
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            next_x, next_y = x + dx[i], y + dy[i]
            if check(next_x, next_y):
                queue.append((next_x, next_y))
                visited[next_x][next_y] = 1
                
                

visited[0][0] = 1
queue.append((0, 0))
BFS()
print(visited[N-1][M-1])