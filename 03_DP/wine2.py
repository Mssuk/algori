arr = [0] * 10001
dp = [[0] * 3 for i in range(10001)]
cnt = int(input())
for i in range(cnt):
    arr[i] = int(input())

'''
상태 0 상태 1 상태 2
------------------
상태 0: n번째 포도잔을 연속으로 0번 먹은 상태인 경우
상태 1: n번째 포도잔을 1번 연속으로 먹은 상태인 경우
상태 2: n번째 포도잔을 2번 연속으로 먹은 상태인 경우
'''

dp[1][1] = arr[1]

dp[2][0] = arr[1]
dp[2][1] = arr[2]
dp[2][2] = arr[1] + arr[2]

for i in range(3, cnt + 1):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])  # n-1번째에는 3가지 상태 모두 올 수 있다.
    dp[i][1] = dp[i - 1][0] + arr[i]  # n번째가 1번 먹은 상태이면 n-1번째는 먹지 않은 상태이어야 한다.
    dp[i][2] = dp[i - 1][1] + arr[i]  # n번째가 2번 먹은 상태이면 n-1번째는 1번 먹은 상태이어야 한다.

print(max(dp[cnt][0], dp[cnt][1], dp[cnt][2]))
