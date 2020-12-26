ability = [1, 2, 2, 4]
money = [3, 1, 4, 2]

N = len(ability)
sum = sum(ability)
dp = [[-1 for i in range(sum+1)] for j in range(N)]
dp[0][ability[0]] = money[0]
for i in range(1, N):
    for j in range(1, sum+1):
        if j < ability[i]:
            dp[i][j] = -1
        else:
            p1 = dp[i - 1][j]
            p2 = -1
            if (dp[i - 1][j - ability[i]] != -1):
                p2 = dp[i - 1][j - ability[i]] + money[i]
            if p1 == -1 or p2 == -1:
                if p1 == -1:
                    dp[i][j] = p2
                else:
                    dp[i][j] = p1
            else:
                dp[i][j] = min(p1, p2)
ans = []
for j in range(sum+1):
    if dp[N - 1][j] != -1:
        ans.append(dp[N - 1][j])
print(min(ans))