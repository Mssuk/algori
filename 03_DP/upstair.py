n = int(input())
li = [0] * 301
for i in range(n):
    li[i] = int(input())

dp = [0] * 301

dp[0], dp[1], dp[2] = li[0], max(
    li[0] + li[1], li[1]), max(li[0] + li[2], li[1] + li[2])

for i in range(3, n):
    dp[i] = max(dp[i - 2] + li[i], dp[i - 3] + li[i - 1] + li[i])


print(dp[n - 1])