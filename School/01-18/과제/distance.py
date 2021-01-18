N = int(input())
d = []
for i in range(N):
    a , b = map(int, input().split())
    d.append([abs(a)+abs(b), i+1])
d.sort(key = lambda x: (x[0],x[1]))
for i in d:
    print(i[1])