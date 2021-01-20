N = int(input())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

dx = [0, 2]
dy = [0, 2]

max_ = 0
count = 0
while True:
    temp = 0
    for i in range(dx[0], dx[1]+1):
        for j in range(dy[0], dy[1]+1):
            temp += grid[i][j]
    if max_ < temp: max_ = temp

    if dy[1] + 1 <= N -1:
        dy[0] += 1
        dy[1] += 1
    else:
        dy = [0, 2]
        if dx[1] + 1 <= N -1:
            dx[0] += 1
            dx[1] += 1
    
    if dx[1] == N -1 and dy[1] == N -1:
        break
print(max_)
    

"""
n=int(input())
square=[list(map(int,input().split())) for _ in range(n)]
posx,posy=2,2
def findGold(posx,posy):
    gold=0
    for x in range(posx-2,posx+1):
        for y in range(posy-2,posy+1):
            if square[y][x]==1:
                gold+=1
    return gold
max_gold=0
for x in range(posx,n):
    for y in range(posy,n):
        max_gold=max(max_gold,findGold(x,y))
print(max_gold)
"""