N = int(input())
genga = [int(input()) for _ in range(N)]
bomb = [list(map(int, input().split())) for _ in range(2)]


for i in range(2):
    genga = genga[:bomb[i][0]-1] + genga[bomb[i][1]:]
print(len(genga))
for i in genga:
    print(i)