# n = 5
# pinballMap = """1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1"""

# 입력 string map을 이중배열 map으로 변환
n = int(input())
ballmap = [list(map(int, input().split())) for _ in range(n)]

# (y, x)
direction = [[0,1], [0,-1], [1,0], [-1,0]] # 동, 서, 남, 북
answer = n+1
count = 0


def nextPosition(current_pos, direct):    
    global direction, count
#     print(current_pos)
    
    next_pos = [current_pos[0] + direct[0], current_pos[1] + direct[1]]
    
    if (0 <= next_pos[0] < n) and (0 <= next_pos[1] < n):
        # 1위치에서 방향 변화
        if ballmap[next_pos[0]][next_pos[1]] == 1:
            if direct == direction[0]: next_dir = direction[3]
            elif direct == direction[1]: next_dir = direction[2]
            elif direct == direction[2]: next_dir = direction[1]
            else: next_dir = direction[0]

        # 2위치에서 방향 변화
        elif ballmap[next_pos[0]][next_pos[1]] == 2:
            if direct == direction[0]: next_dir = direction[2]
            elif direct == direction[1]: next_dir = direction[3]
            elif direct == direction[2]: next_dir = direction[0]
            else: next_dir = direction[1]
        # 0위치에서 방향 변화
        else: next_dir = direct
    
    else: next_dir = direct
    
    # 한번 진행
    count = count + 1
            
    return next_pos, next_dir

start_positions = [[-1, i] for i in range(n)]
start_positions.extend([[n, i] for i in range(n)])
start_positions.extend([[i, -1] for i in range(n)])
start_positions.extend([[i, n] for i in range(n)])
start_positions = [[4,-1]]


for start in start_positions:
    # 시작시 방향 설정
    if start[0] == -1: start_direction = direction[2]
    elif start[0] == n: start_direction = direction[3]
    elif start[1] == -1: start_direction = direction[0]
    else: start_direction = direction[1]
    
    # 1회 실행
    current, current_direction = nextPosition(start, start_direction)

    # 나올때까지 진행
    while((0 <= current[0] < n) and (0 <= current[1] < n)):
        current, current_direction = nextPosition(current, current_direction)

    # 최댓값 update
    if count > answer: answer = count
    count = 0
# print(current)
print(answer)