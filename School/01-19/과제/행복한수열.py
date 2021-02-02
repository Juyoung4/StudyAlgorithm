n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]

total = 0
for i in range(n):
    for j in range(n-m+1): # column
        if len(set(nums[i][j:j+m])) == 1: 
            total += 1
            break
    for j in range(n-m+1): # row
        temp = [k[i] for k in nums[j:j+m]]
        if len(set(temp)) == 1: 
            total += 1
            break

print(total)