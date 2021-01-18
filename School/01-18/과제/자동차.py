N = int(input())
years = list(map(int, input().split()))

min_ = years[0]
total = 0
for i in range(1, N):
    if i == 1:
        total = max(years[i:]) - years[i]
    else:
        temp = max(years[i:]) - years[i]
        if total < temp:
            total = temp
print(total)
