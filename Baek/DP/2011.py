# 2011 - 암호코드

if __name__ == "__main__":
    code = [int(s) for s in input()]
    print(code)
    len_c = len(code)
    if code[0] == 0:
        print(0)
    else:
        dp = [0]*(len_c+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len_c+1):
            cur = code[i-1] # 한 자리
            cur2 = code[i-2] * 10 + code[i-1] # 두 자리
            if cur >= 1 and cur <= 9:
                dp[i] += dp[i-1]
            if cur2 >= 10 and cur2 <= 26:
                dp[i] += dp[i-2]
            dp[i] = dp[i]%1000000

        print(dp[-1])