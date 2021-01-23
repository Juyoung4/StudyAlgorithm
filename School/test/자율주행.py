n, m = map(int, input().split())
x, y, cur_dir = map(int, input().split())

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 
# idx = 0 북 동 남 서 
left = [3, 0, 1, 2]

# 후진
# idx = 0 북 동 남 서
down = [2, 3, 0, 1]

dir_check = [0, 0, 0, 0]

roads = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

def inRange(x, y):
    return 0 <= x < n and 0 <= y < m

def total_roads():
    global cur_dir, dir_check
    global x, y
    visited[x][y] = 1
    #dir_check[cur_dir] = 0
    count = 1
    while True:
        #print("cur visited : ", visited)
        print("(cur direction, dir_check) : ", (cur_dir, dir_check))
        if sum(dir_check) < 4:
            # step 1: 현재 방향 - 왼쪽 방향 check
            next_x, next_y = x + dx[left[cur_dir]], y + dy[left[cur_dir]]
            if inRange(next_x, next_y):
                if not visited[next_x][next_y] and not roads[next_x][next_y]: # 방문한적 x, 인도 x
                    x, y = next_x, next_y
                    dir_check = [0,0,0,0]
                    visited[next_x][next_y] = 1
                    cur_dir = left[cur_dir]
                    count += 1
                else: # step2 : 방문한적 o or 인도 o
                    cur_dir = left[cur_dir]
                    dir_check[cur_dir] = 1
        else: # step 3 : 전진 x -> 바라보는 방향 유지 + 한 칸 후진
            dir_check = [0,0,0,0]
            next_x, next_y = x + dx[down[cur_dir]], dy[down[cur_dir]]
            # 만약에 인도 x -> 후진 o
            if inRange(next_x, next_y) and not roads[next_x][next_y]:
                x, y= next_x, next_y
            else: # 만약에 인도 o -> 후진 x
                break
    return count


print(total_roads())


        