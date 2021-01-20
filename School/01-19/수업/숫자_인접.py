N, x, y = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

x -= 1
y -= 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total = []

while True:
    total.append(grid[x][y])
    
    max_x, max_y = x, y
    for i in range(4):
        if (x+dx[i] in range(0,N) and y+dy[i] in range(0,N)) and grid[max_x][max_y] < grid[x+dx[i]][y+dy[i]]: 
            x, y = x+dx[i], y+dy[i]
            break
    else:
        break
for i in total:
    print(i, end=' ')