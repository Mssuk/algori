# dp = [0] * 91
#
# dp[1] = 1
# dp[2] = 1
#
# n = int(input())
# for i in range(3, n+1):
#     dp[i] = dp[i-1] + dp[i-2]
# print(dp[n])

dp = [[0] * 2 for _ in range(91)]
dp[1][1] = 1
dp[2][0] = 1
n = int(input())
for i in range(3, n+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]
print(sum(dp[n]))

