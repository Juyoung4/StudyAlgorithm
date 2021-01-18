N = int(input())
grid = [[0 for _ in range(N)] for _ in range(N)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
temp = [0,1,1,1]
limit = [1,1,2,2]
c_dir, num = 0, 1
x, y = N//2, N//2
while True:
    grid[x][y] = num
    num += 1
    
    if temp[c_dir] == limit[c_dir]:
        limit[c_dir] += 2
        temp[c_dir] = 1
        if c_dir == 3:
            c_dir = 0
        else:
            c_dir += 1
    else:
        temp[c_dir] += 1

    x += dx[c_dir]
    y += dy[c_dir]

    if num == (N*N)+1: break
for i in grid:
    for j in i:
        print(j,end=' ')
    print('')
    
        