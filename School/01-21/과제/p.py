from collections import deque

n, k, u, d = map(int, input().split())
if k > 3:
    k = min(n, 3)
citys = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
result = []
queue = deque([])

def find_max():
    max_ = -1
    for x in range(n):
        for y in range(n):
            max_ = max(max_, visited[x][y])
    return max_

def inRange(x, y):
    return 0 <= x < n and 0 <= y < n

def check(x, y):
    return inRange(x,y) and not visited[x][y] and citys[x][y] and visited[x][y] != -1

def push(x, y, d):
    queue.append((x, y))
    visited[x][y] = d

def BFS():
    global visited
    # direction -상 하 좌 우
    dx = (-1, 1, 0 , 0)
    dy = (0, 0, 1, -1)
    
    for k in range(n):
        #print("start point !!", point)
        for p in range(n):
            push(k, p, 1)
            while queue:
                x, y = queue.popleft()
                count = 0
                for i in range(4):
                    next_x, next_y = x + dx[i], y + dy[i]
                    if check(next_x, next_y):
                        next_height = abs(citys[x][y] - citys[next_x][next_y])
                        if (u <= next_height) and (next_height <= d):
                            count += 1
                            push(next_x, next_y, visited[x][y]+count)
            #print(visited)
            if len(visited[0]) != 1 and (x == k) and (y == p):
                result.append(0)
            else:
                result.append(find_max())
            visited = [[0 for _ in range(n)] for _ in range(n)]
BFS()

result = sorted(set(result), reverse=True)
#print(result)
print(k)
result = sum(result[:k])
print(result)
