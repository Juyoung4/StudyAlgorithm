result = 0
s, e = map(int, input().split())
for i in range(s, e+1):
    if i in (1,2,3): continue
    temp = 1
    for j in range(2, i):
        if not i % j: temp += j
    if temp == i: 
        result += 1
print(result)