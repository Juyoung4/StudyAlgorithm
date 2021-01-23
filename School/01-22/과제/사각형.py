n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

def max_one_two(arr):
    second = smallest = float('inf')
    for n in arr:
        if n < smallest:
            second = smallest
            smallest = n
        elif smallest < n < second :
            second = n
    return [smallest, second]

def initailize():
    dp[0][0] = [grid[0][0], grid[0][0]]
    # 아래 방향
    for i in range(1, n):
        #print(dp[i-1][0])
        arr = dp[i-1][0] + [grid[i][0]]
        dp[i][0] = max_one_two(arr)
        arr = dp[0][i-1] + [grid[0][i]]
        dp[0][i] = max_one_two(arr)

initailize()
for i in range(1,n):
    for j in range(1,n):
        if i != n-1 or j != n-1:
            dp[i][j] = max_one_two(dp[i-1][j] + dp[i][j-1] + [grid[i][j]])
        else:
            if grid[i][j] < dp[i-1][j][0] and grid[i][j] < dp[i-1][j][1] and grid[i][j] < dp[i][j-1][0] and grid[i][j] < dp[i][j-1][1]:
                dp[i][j] = [grid[i][j], grid[i][j]]
            else:
                dp[i][j] = max_one_two(dp[i-1][j] + dp[i][j-1])

print(dp)
result = dp[-1][-1]
if float('inf') == result[0]:
    print(result[1])
elif float('inf') == result[1]:
    print(result[0])
else:
    print(max(dp[-1][-1]))
    