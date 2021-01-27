N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
def inRange(x, y):
    return 0 <= x < N and 0 <= y < N

# check할것 같은 숫자 인지, 새로운 숫자이면 visited 다시 정의해서 넘기기
def check(x, y, checks):
    if not inRange(x, y): return False
    if visited[x][y] or grid[x][y] != checks: return False
    else:
        return True

def DFS(x, y, checks):
    #print(visited)
    # direction
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    block = 1
    for i in range(4):
        next_x, next_y = x + dx[i], y + dy[i]
        if check(next_x, next_y, checks):
            visited[next_x][next_y] = 1
            block += DFS(next_x, next_y, checks)
    return block

bomb, max_count = 0, -1

for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            visited[x][y] = 1
            block = DFS(x, y, grid[x][y])
            if block > 3: bomb += 1
            max_count = max(max_count, block)
print(bomb, max_count)