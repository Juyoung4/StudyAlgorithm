n, k, u, d = map(int, input().split())
citys = [list(map(int, input().split())) for _ in range(n)]

visited = [0 for _ in range(n*n)] # 방문한 곳 check

# 각 K개에서 갈 수 있는 도시 수 COUNT
def BFS(*args):
    pass

def find_combi(cur_num, last_num):
    if cur_num == k:
        temp = []
        for i in range(n*n):
            if visited[i]:
                # 점의 위치 계산
                # X = i // n, Y = i % n
                temp.append([i//n, i%n])
        # 구한 조합에서 travel BFS Start
        BFS(temp)
        return

    for i in range(last_num+1, n*n):
        visited[i] = 1
        find_combi(cur_num+1, i)
        visited[i] = 0

# 나올 수 있는 순열 조합
for i in range(n*n):
    visited[i] = 1
    find_combi(1, i)
    visited[i] = 0