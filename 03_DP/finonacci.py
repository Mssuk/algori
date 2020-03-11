dp = [[0] * 2 for i in range(41)]

dp[0][0], dp[0][1] = 1, 0
dp[1][0], dp[1][1] = 0, 1

for i in range(2, len(dp)):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

cnt = int(input())
for i in range(cnt):
    num = int(input())
    print(dp[num][0], dp[num][1])


