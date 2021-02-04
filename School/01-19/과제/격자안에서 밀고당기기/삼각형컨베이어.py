n, t = map(int, input().split())
belts = [list(map(int, input().split())) for _ in range(3)]

while t:
    belts[1].insert(0, belts[0].pop())
    belts[2].insert(0, belts[1].pop())
    belts[0].insert(0, belts[2].pop())
    t -= 1

for belt in belts:
    for b in belt:
        print(b, end=' ')
    print()