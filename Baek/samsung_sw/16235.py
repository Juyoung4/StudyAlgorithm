# 16235 나무 재테크
import sys

if __name__ == "__main__":
    N, M, K = map(int, sys.stdin.readline().split())
    basic_adds = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    grounds = [[[] for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        x, y, z = map(int, sys.stdin.readline().split())
        grounds[x-1][y-1].append(z)
    tree_adds = [[5 for _ in range(N)] for _ in range(N)] # 나무의 양분 복사
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, 1), (1, -1), (-1, -1)]

    for _ in range(K):
        # 1. 봄 + 여름 + 겨울
        for i in range(N):
            for j in range(N):
                if not grounds[i][j]: tree_adds[i][j] += basic_adds[i][j]
                else :
                    new_tree, len_n= [], 0
                    len_g = len(grounds[i][j])
                    for g in range(len_g):
                        if tree_adds[i][j] - grounds[i][j][g] >= 0:
                            tree_adds[i][j] -= grounds[i][j][g]
                            new_tree.append(grounds[i][j][g]+1)
                            len_n += 1
                        else:
                            for k in range(g, len_g):
                                tree_adds[i][j] += (grounds[i][j][k]//2)
                            break
                    grounds[i][j] = new_tree
                    # 4. 겨울 양분 더하기
                    tree_adds[i][j] += basic_adds[i][j]
        # 3. 가을
        # 번식 할 수 있는 나무 = 나무의 나이가 5의 배수
        for i in range(N):
            for j in range(N):
                if grounds[i][j]:
                    for age in grounds[i][j]:
                        if age % 5 == 0:
                            for dx, dy in dirs:
                                nr, nc = i+dx, j+dy
                                if 0 <= nr < N and 0 <= nc < N:
                                    grounds[nr][nc] = [1]+grounds[nr][nc] # insert 시간 초과 사용 x

    total = 0
    for i in range(N):
        for j in range(N):
            total += len(grounds[i][j])
    print(total)
