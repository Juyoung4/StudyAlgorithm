# 사다리 조작 (https://www.acmicpc.net/problem/15684)
import sys

max_ = 4

def check(cur_len, cur_num): # cur_len 전체 길이, cur_num=현재 True한 개수
    global max_
    if cur_len >= max_:
        return

    if move_check():
        max_ = cur_len
        return

    for idx in range(cur_num+1, len_c):
        r, c = candidates[idx]
        if not visited[r][c-1] and not visited[r][c+1]:
            visited[r][c] = True
            check(cur_len + 1, idx)
            visited[r][c] = False

def move_check():
    for i in range(1, N+1): #왜냐하면 세로로 떨어지기 때문
        temp = i
        for j in range(1, H+1):
            if visited[j][temp]:
                temp += 1
            elif visited[j][temp-1]:
                temp -= 1
        if temp != i: return False
    return True

if __name__ == "__main__":
    N, M, H = map(int, sys.stdin.readline().split())
    visited = [[False for _ in range(N+1)] for _ in range(H+1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        visited[a][b] = True

    candidates =[]
    for i in range(1, H+1):
        for j in range(1, N):
            if not visited[i][j-1] and not visited[i][j] and not visited[i][j+1]:
                candidates.append((i, j))

    len_c = len(candidates)

    check(0, -1)
    


    if max_ < 4: print(max_)
    else: print(-1)




