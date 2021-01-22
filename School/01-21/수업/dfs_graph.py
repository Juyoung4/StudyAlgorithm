N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for edge in edges:
    graph[edge[0]][edge[1]] = 1
    graph[edge[1]][edge[0]] = 1

cnt = 0

def DFS(vertex):
    global cnt
    for cur_v in range(1, N+1):
        if graph[vertex][cur_v] and not visited[cur_v]:
            visited[cur_v] = True
            cnt += 1
            DFS(cur_v)
            

def solution():
    # 1번에서 시작
    visited[1] = True
    DFS(1)

solution()
print(cnt)