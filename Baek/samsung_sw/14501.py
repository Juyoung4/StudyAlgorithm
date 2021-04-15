# 퇴사 https://www.acmicpc.net/problem/14501
import sys
N = int(sys.stdin.readline())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [0]*(N+1)
for i in range(N-1, -1, -1):
    if i+table[i][0] > N: dp[i] = dp[i+1]
    else: dp[i] = max(table[i][1]+dp[i+table[i][0]], dp[i+1])
print(dp[0])
