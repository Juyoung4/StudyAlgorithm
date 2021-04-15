# 로봇청소기 https://www.acmicpc.net/problem/14503
import sys
N, M = map(int, sys.stdin.readline().split())
r, c, next_dir = map(int, sys.stdin.readline().split())
grids = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 0-북, 1-동, 2-남, 3-서
# 북->동, 동->남, 남->서, 서->북
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def clean(next_dir, r, c, total):
    while True:
        check = False
        for _ in range(4): # 4방향 모두 check
            next_dir = (next_dir+3)%4 # 왼쪽 방향 의미
            next_r, next_c = r+dirs[next_dir][0], c+dirs[next_dir][1]
            if 0 <= next_r < N and 0 <= next_c < M:
                # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면
                if not grids[next_r][next_c]:
                    total += 1
                    grids[next_r][next_c] = 2
                    r, c = next_r, next_c
                    check = True
                    break
        if not check: # 네 방향 모두 청소가 이미 되어있거나 벽인 경우
            t1, t2 = r-dirs[next_dir][0], c-dirs[next_dir][1]
            if grids[t1][t2] != 1:
                r, c = t1, t2
            else: return total

if __name__ == "__main__":
    grids[r][c] = 2
    print(clean(next_dir, r, c, 1))
