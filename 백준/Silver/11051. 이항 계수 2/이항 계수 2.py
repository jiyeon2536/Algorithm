# 이항 계수 2
n, k = map(int, input().split())

dp = [[0] * (n+1) for _ in range(n+1)]

# dp 초기회
for i in range(n+1):
    dp[i][0] = 1
    dp[i][1] = i
    dp[i][i] = 1


for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]


print(dp[n][k] % 10007)
