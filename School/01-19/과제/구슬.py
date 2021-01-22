import logging
N, bN, t = map(int, input().split())
balls = []

#하 우 상 좌
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(bN):
    r, c, d, w = input().split()
    if d == 'L': d = 1
    elif d == 'R': d = 3
    elif d == 'U' : d = 2
    else: d = 0
    balls.append([int(r)-1, int(c)-1, d, int(w), i])

def inRrange(c, r):
    return 0 <= c < N and 0 <= r < N

while t:
    check_ball = dict()
    count = 0
    for ball in balls:
        if inRrange(ball[0]+dx[ball[2]], ball[1]+dy[ball[2]]):
            ball[0] += dx[ball[2]]
            ball[1] += dy[ball[2]]
        else:
            if ball[2] == 0: ball[2] = 2
            elif ball[2] == 1: ball[2] = 3
            elif ball[2] == 2: ball[2] = 0
            else: ball[2] = 1
        temp = (ball[0], ball[1])
        if temp not in check_ball.keys():
            check_ball[temp] = [ball[4]]
        else:
            check_ball[temp].append(ball[4])

    temp2, check, temp3 = [], False, []
    for key, value in check_ball.items():
        if len(value) > 1:
            w, idx = 0, max(value)
            for ball in balls:
                if ball[4] in value:
                    temp2.append(ball[4])
                    w += ball[3]
                if ball[4] == idx: d = ball[2]
            temp3.append([key[0], key[1], d, w, idx])
            check = True
    if check: 
        balls = [balls[i] for i in range(len(balls)) if i not in temp2] + temp3
    
    t -= 1

balls.sort(key=lambda x: -x[3])
print(len(balls), balls[0][3])