N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

bomb_c = 0
#하 오 상 왼
# 오 왼 하 오
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
count = 0
max_ = 0
def inRrange(c, r):
    return 0 <= c < N and 0 <= r < N

def count_pair(x, y, tgrid):
    count = 0
    check = tgrid[x][y]
    if not check: return count
    next_x, next_y = x+dx[0], y+dy[0]
    if inRrange(next_x, next_y):
        if check == tgrid[next_x][next_y]: 
            count += 1
    return count

def bombs(tgrid, level, cur_x, cur_y):
    cgrid = [[0 for _ in range(N)] for _ in range(N)]
    temps = []
    count = 0
    temps.append((cur_x, cur_y))
    for d in range(4):
        for _ in range(level):
            cur_x += dx[d]
            cur_y += dy[d]
            if inRrange(cur_x, cur_y):
                temps.append((cur_x, cur_y))
    for col in range(N):
        temp = []
        for row in range(N):
            if (row, col) not in temps:
                temp.append(tgrid[row][col])
        for row in range(len(temp)):
            cgrid[-(row+1)][col] = temp[-(row+1)]
            
            if -(row+2) >= -(len(temp)):
                if temp[-(row+2)] == temp[-(row+1)]:
                    count += 1
    for x in range(N):
        for y in range(N):
            count += count_pair(x, y, cgrid)
    return count

for i in range(N):
    for j in range(N):
        for k in range(N):
            max_ = max(max_, bombs(grid, k, i, j))
            
print(max_)