N, move_c, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
moves = [list(map(int, input().split())) for _ in range(move_c)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = [[0 for i in range(N)] for j in range(N)]
for i in moves:
    count[i[0]-1][i[1]-1] = 1
    
while t:
    n_count = [[0 for _ in range(N)] for _ in range(N)]

    # next_count 배열 생성 - max값 찾기
    for x in range(N):
        for y in range(N):
            if not count[x][y]: continue
            else:
                max_x, max_y = -1, -1
                for i in range(4):
                    if x + dx[i] in range(N) and y + dy[i] in range(N):
                        if (max_x < 0 and max_y < 0):
                            max_x, max_y = x+dx[i], y+dy[i]
                        else:
                            if grid[max_x][max_y] < grid[x+dx[i]][y+dy[i]]:
                                max_x, max_y = x+dx[i], y+dy[i]
                        
                n_count[max_x][max_y] += 1

    if n_count == count: break
    for i in range(N):
        for j in range(N):
            if n_count[i][j] == 1:
                count[i][j] = 1
            else:
                count[i][j] = 0

    # 초 감소
    t -= 1

total = 0
for i in range(N):
    for j in range(N):
        if count[i][j] == 1:
            total += 1
print(total)