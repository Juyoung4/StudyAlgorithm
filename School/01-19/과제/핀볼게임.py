N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

#하 우 상 좌
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
one = [1, 0, 3, 2]
two = [3, 2, 1, 0]
direction = [3, 0, 1, 2] # add direction

x, y = 0, 0
max_count = 1
cur_d = 0

for d in direction:
    for i in range(N):
        count = 1
        idx = cur_d
        cur_x, cur_y = x, y
        while True:
            if (cur_x + dx[idx] in range(N)) and (cur_y + dy[idx] in range(N)):
                temp = grid[cur_x + dx[idx]][cur_y + dy[idx]]
                p_idx = idx
                if temp == 1:
                    idx = one[idx]
                elif temp == 2:
                    idx = two[idx] 
                cur_x += dx[p_idx]
                cur_y += dy[p_idx]
                count += 1
            else:
                break
        if max_count < count: 
            max_count = count
        if i != N-1:
            x += dx[direction[cur_d]]
            y += dy[direction[cur_d]]
    cur_d += 1
print(max_count+1)