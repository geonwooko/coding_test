def solution(n):
    answer = 0
    mod = 10**9+7
    dp = [0] * (n+1)
    
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = (dp[i-2] + dp[i-1]) % mod
    
    return dp[n]