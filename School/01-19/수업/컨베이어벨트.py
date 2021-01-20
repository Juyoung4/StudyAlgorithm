N, t = map(int, input().split())
belt1 = list(map(int, input().split()))
belt2 = list(map(int, input().split()))[::-1]

for i in range(t):
    belt2.append(belt1.pop())
    belt1.insert(0, belt2.pop(0))

for i in belt1:
    print(i, end=' ')
print()
for i in belt2[::-1]:
    print(i, end=' ')