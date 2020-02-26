# O(N^2)
cnt = int(input())
li = list(map(int, input().split()))

dp = [0] * 1001
for i in range(0, cnt):
    dp[i] = 1
    for j in range(0, i):
        if li[j] > li[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
