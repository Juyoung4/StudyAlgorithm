# 땅따먹기

def solution(land):
    answer = 0
    r = len(land)
    if r == 1: return max(land[0])
    
    dp = land[0]
    
    for i in range(1, r):
        a, b, c, d = 0, 0, 0, 0
        temp_land = land[i]

        a = temp_land[0] + max(dp[1:])
        b = temp_land[1] + max([dp[0]] + dp[2:])
        c = temp_land[2] + max(dp[:2]+[dp[3]])
        d = temp_land[3] + max(dp[:3])
        
        dp[0], dp[1], dp[2], dp[3] = a, b, c, d
        
    return max(dp)