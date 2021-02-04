n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
box1_x = [0, 1, 1]
box1_y = [1, 1, 0]
max_ = 0
for i in range(n):
    for j in range(m):
        # 4개 격자안에 최대 찾기
        temp = [grid[i][j]]
        for k in range(3):
            t_x, t_y = i+box1_x[k], j+box1_y[k]
            if t_x < n and t_y < m: temp.append(grid[t_x][t_y])
            else: break
        else:
            temp.sort(reverse=True)
            s = sum(temp[:3])
            if max_ < s: max_ = s
        del temp
        
        # 3개 이어진 것 최대 찾기 - 가로, 세로
        t_x, t_y = i+2, j+2
        if t_y < m: #가로
            s = sum(grid[i][j:t_y+1])
            if max_ < s: max_ = s
        if t_x < n: #세로
            s = 0
            for k in range(i, t_x+1):
                s += grid[k][j]
            if max_ < s: max_ = s
print(max_)