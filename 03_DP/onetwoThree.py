cnt = int(input())
li = []
for i in range(cnt):
    li.append(int(input()))

print(li)

dp = [0]*11
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in li:
    for j in range(3, i+1):
        dp[j] = dp[j-3] + dp[j-2] + dp[j-1]
    print(dp[i])
