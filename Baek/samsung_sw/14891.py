#톱니바퀴 https://www.acmicpc.net/problem/14891
import sys

def change(gears, ts):
    for i in range(4):
        if ts[i] == 0: continue
        elif ts[i] == 1: # 시계방향 회전
            temp = gears[i][-1]+gears[i][:-1]
        else: # 반시계 방향 회전
            temp = gears[i][1:]+gears[i][0]
        gears[i] = temp
    return gears

def turn(gears, turns, turn_num):
    for i in range(turn_num):
        cur_num = turns[i][0]-1
        ts = [0, 0, 0, 0]
        ts[cur_num] = turns[i][1] # 해당 위치 회전
        if cur_num ==0: # 1, 4번 톱니 회전 
            for j in range(1, 4):
                if gears[j-1][2] != gears[j][6]: # 전이 회전하고 현재 마주보는게 같으면
                    ts[j] = ts[j-1]*(-1)
                else:
                    break
        elif cur_num == 1:
            if gears[cur_num-1][2] != gears[cur_num][6]: 
                ts[cur_num-1] = ts[cur_num]*(-1)
                if gears[cur_num-2][2] != gears[cur_num-1][6]: 
                    ts[cur_num-2] = ts[cur_num-1]*(-1)
            if gears[cur_num][2] != gears[cur_num+1][6]:
                ts[cur_num+1] = ts[cur_num]*(-1)
        elif cur_num == 2:
            if gears[cur_num-1][2] != gears[cur_num][6]:
                ts[cur_num-1] = ts[cur_num]*(-1)
            if gears[cur_num][2] != gears[cur_num+1][6]:
                ts[cur_num+1] = ts[cur_num]*(-1)
                if ts[cur_num-1] and gears[cur_num+1][2] != gears[cur_num+2][6]:
                    ts[cur_num+2] = ts[cur_num+1]*(-1)
        else:
            for j in range(3, 0, -1):
                if gears[j-1][2] != gears[j][6]: # 전이 회전하고 현재 마주보는게 같으면
                    ts[j-1] = ts[j]*(-1)
                else:
                    break
        gears = change(gears, ts) # gears 돌아감

    return int(gears[0][0])*1 + int(gears[1][0])*2 + int(gears[2][0])*4 + int(gears[3][0])*8

if __name__ == "__main__":
    # N극은 0, S극은 1
    # 12시방향부터 시계방향 순서대로 주어짐
    gears = [sys.stdin.readline()[:-1] for _ in range(4)]
    turn_num = int(sys.stdin.readline())

    # 인덱스0: 톱니바퀴 번호, 인덱스1: 방향
    # 시계방향 = 1, 반시계방향 = -1
    turns = [list(map(int, sys.stdin.readline().split())) for _ in range(turn_num)]

    result = turn(gears, turns, turn_num)
    print(result)
