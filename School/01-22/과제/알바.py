import sys
INT_MIN = -sys.maxsize

n = int(input())
work = [list(map(int, input().split())) for _ in range(n)]
for _ in range(n)
dp = [INT_MIN for _ in range(n+1)]

# 순서x
dp[0] = 0
temp = [0] + work
for i in range(1,n+1):
    for j in range(i):
        #if dp[i] == INT_MIN: continue
        if temp[j] < temp[i]:
            dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
print(max(dp))