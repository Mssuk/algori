cnt = int(input())
for _ in range(cnt):
    col = int(input())
    dp = [[0] * 100001 for i in range(2)]
    li = []
    for i in range(2):
        li.append(list(map(int, input().split())))

    li[0].insert(0, 0)
    li[1].insert(0, 0)
    dp[0][1] = li[0][1]
    dp[1][1] = li[1][1]

    for i in range(2, col + 1):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + li[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + li[1][i]

    print(max(dp[0][col], dp[1][col]))
