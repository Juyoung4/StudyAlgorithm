x, y = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(x)]

def find_Max(x1, y1, dx, dy):
    check, total = True, 0
    for i in range(x1-dx, x1+1):
        for j in range(y1-dy, y1+1):
            if grid[i][j] <= 0: 
                check = False
                break
            total += 1
        if not check: return (check, total)
    if check: return (check, total)
    
max_x, max_y, count = 0, 0, -1
for dx in range(x):
    for dy in range(y):
        for t_x in range(dx, x):
            for t_y in range(dy, y):
                result = find_Max(t_x, t_y, dx, dy)
                if result[0]: 
                    if count < result[1]: count = result[1]
print(count)