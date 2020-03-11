n = int(input())
li = list(map(int, input().split()))

dp = [0] * (n+1)


for i in range(0, len(li)):
    dp[i] = li[i]
    fls = list(map(lambda v: dp[v], filter(lambda x: li[x] < li[i], range(0, i))))
    if fls:
        dp[i] += max(fls)

print(dp)
print(max(dp))
