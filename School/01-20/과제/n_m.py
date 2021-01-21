n, m = map(int, input().split())
vertex = [tuple(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n+1)]

min_ = -1

def find_min(combi):
    global min_
    max_ = 0
    for i in range(len(combi)):
        for j in range(i+1, len(combi)):
            temp = abs(combi[i][0] - combi[j][0])**2 + abs(combi[i][1] - combi[j][1])**2
            if not i and not j: max_ =  temp
            else:
                max_ = max(max_, temp)
    if min_ == -1:
        min_ = max_
    else:
        min_ = min(min_, max_)
    return
                            
def find_combi(cur_num, last_num):
    if cur_num == m:
        temp = []
        for i in range(1, n+1):
            if visited[i]:
                temp.append(vertex[i-1])
        find_min(temp)
        return

    for i in range(last_num+1, n+1):
        visited[i] = 1
        find_combi(cur_num+1, i)
        visited[i] = 0

# 나올 수 있는 순열 조합
for i in range(1, n+1):
    visited[i] = 1
    find_combi(1, i)
    visited[i] = 0
print(min_)
