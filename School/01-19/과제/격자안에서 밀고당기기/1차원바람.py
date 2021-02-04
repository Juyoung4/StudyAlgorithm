N, M, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
temp = input().split()
r, d = int(temp[0])-1, 1 if temp[1] == 'L' else -1

def move(t_r, t_d):
    # 현재 행 위치에서 바람에 방향에 맞게 움직이기
    if t_d == 1:
        temp = grid[t_r].pop()
        grid[t_r].insert(0, temp)
    else:
        temp = grid[t_r].pop(0)
        grid[t_r].append(temp)

def check_wind(r_p, r):
    for p, c in zip(grid[r_p], grid[r]):
        if p==c: 
            print(p,c)
            return True
    return False

def wind(cur_r, dire):
    move(cur_r, dire)
    
    r1, r2 = cur_r-1, cur_r+1 #위쪽, 아래쪽
    r1_p, r2_p = cur_r, cur_r
    d1, d2 = dire, dire
    status1, status2 = True, True
    count = 0
    while status1:
        print("check 1 : ", r1_p, r1, d1)
        if check_wind(r1_p, r1):
            d1 *= -1
            move(r1, d1)
            r1_p, r1 = r1, r1-1
        else:
            status1 = False
        if r1_p == 0: status1 = False
        print(grid)

    while status2:
        print("check 2 : ", r2_p, r2, d2)
        if check_wind(r2_p, r2):
            print("origi: ", r2_p, r2)
            d2 *= -1
            move(r2, d2)
            r2_p, r2 = r2, r2+1
            print("change : ",r2_p, r2)
        else:
            status2 = False
        if r2 == N: status2 = False
        count +=1
        if count == 9 : break
        print(grid)
    
wind(r, d)
for i in grid:
    for j in i:
        print(j, end = ' ')
    print()