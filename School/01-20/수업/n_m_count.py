k, N = map(int, input().split())
# n, m = 1부터 N 사이의 숫자 중 M개의 숫자를 골라

visited = [0 for _ in range(k+1)]

def print_num():
    for i in range(1, k+1):
        if visited[i]: print(i, end = ' ')
    print()


def find_combi(cur_num, last_num):
    if cur_num == N:
        print_num()
        return

    for i in range(last_num+1, k+1):
        visited[i] = 1
        find_combi(cur_num+1, i)
        visited[i] = 0

# 나올 수 있는 순열 조합
for i in range(1, k+1):
    visited[i] = 1
    find_combi(1, i)
    visited[i] = 0