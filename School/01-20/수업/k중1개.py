k, N = map(int, input().split())

answer = []
def print_num():
    for i in answer:
        print(i, end = ' ')

def choose(k, cur_num):
    if cur_num == N:
        print_num()
        print()
        return

    for i in range(1,k+1):
        answer.append(i)
        choose(k, cur_num + 1)
        answer.pop()

choose(k, 0)