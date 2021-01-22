from collections import deque
n, k = map(int, input().split())
oranges = [list(map(int, input().split())) for _ in range(n)]
visited = [[-3 for _ in range(n)] for _ in range(n)]
q = deque([])
t = deque([])
# 귤 개수 넣기
t.append(k)

def inRange(x, y):
    return 0 <= x < n and 0 <= y < n

def check(x, y):
    # 범위 안에 있는지
    if not inRange(x,y): return False
    if visited[x][y] != -3: return False
    return True

def push(x, y, d):
    if d != -1:
        q.append((x, y))
    visited[x][y] = d

def BFS():
    # direction -상 하 좌 우
    dx = (-1, 1, 0 , 0)
    dy = (0, 0, 1, -1)

    time = 1
    while t:
        count = t.popleft()
        for _ in range(count):
            x, y = q.popleft()
            for i in range(4):
                next_x, next_y = x + dx[i], y + dy[i]
                if check(next_x, next_y):
                    push(next_x, next_y, time)
        if len(q): t.append(len(q))
        time += 1
    

                
# 시작 점 => queue에 넣기
# # 미리 0인 부분 -1로 change
for x in range(n):
    for y in range(n):
        if oranges[x][y] == 2:
            push(x, y, 0)
        if oranges[x][y] == 0:
            push(x, y, -1)


BFS()
# 출력문
for x in range(n):
    for y in range(n):
        if visited[x][y] == -3: print(-2, end = ' ')
        else: print(visited[x][y], end = ' ')
    print()