n, m = map(int, input().split())
car_row, car_col, direction = map(int, input().split())
road = [list(map(int,input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dx = [-1,0,1,0] 
dy = [0,1,0,-1]
def onRoad(row,col):
    return 0 <= row < n and 0 <= col < m and not road[row][col]

def autoDrive(row, col, direct):

    for i in range(1,5):
        m_direct = (direct - i)%4
        l_row, l_col = row + dx[m_direct], col + dy[m_direct]
        if onRoad(l_row, l_col) and not visited[l_row][l_col]:
            visited[l_row][l_col] = True
            autoDrive(l_row,l_col,m_direct)
            return
    #go back
    b_row,b_col = row - dx[direct], col - dy[direct]
    if onRoad(b_row,b_col):
        autoDrive(b_row,b_col, direct)
    
visited[car_row][car_col] = True
autoDrive(car_row, car_col, direction)
answer = 0
for i in visited:
    for j in i:
        if j:
            answer+=1
print(answer)
