n,m = map(int, input().split())
grid = [[0 for _ in range(m)] for _ in range(n)]

num = 0
x, y= 0,0

cur = 0

for i in range(m):
    if not i%2 : 
        for j in range(n):
            grid[j][i] = num
            num += 1
    else:
        for j in range(1,n+1):
            grid[-j][i] = num
            num += 1

for i in range(n):
    for j in range(m):
        print(grid[i][j],end=' ')
    print()