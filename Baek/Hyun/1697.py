# 숨바꼭질
from collections import deque


if __name__ == "__main__":
    N, K = map(int, input().split())

    queue = deque()
    queue.append([N, 0])

    visitied = [-1]*100001

    while queue:
        cur, time = queue.popleft()

        if cur == K:
            print(time)
            break
        next_time = time+1
        # x-1
        if cur-1 >= 0 and (visitied[cur-1] == -1 or visitied[cur-1] > next_time):
            queue.append([cur-1, next_time])
            visitied[cur-1] = next_time
        # x+1
        if cur+1 <= 100000 and (visitied[cur+1] == -1 or visitied[cur+1] > next_time):
            queue.append([cur+1, next_time])
            visitied[cur+1] = next_time
        # x*2
        if 0 < cur*2 <= 100000 and (visitied[cur*2] == -1 or visitied[cur*2] > next_time):
            queue.append([cur*2, next_time])
            visitied[cur*2] = next_time

