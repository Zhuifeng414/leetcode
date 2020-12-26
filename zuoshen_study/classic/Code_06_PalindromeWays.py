class Solution(object):
    def __init__(self):
        return

    def dps(self, arr):
        n = len(arr)
        dp = [[0 for i in range(n+1)] for j in range(n+1)]
        for i in range(n):
            dp[i][i] = 1
            if i+1 < n and arr[i] == arr[i+1]:
                dp[i][i+1] = 3
            else:
                dp[i][i+1] = 2
        # for i,j in zip(x,y) :
        for p in range(2, n):
            for j in range(p, n):
                i = j - p
                if arr[i] == arr[j]:
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]

        return dp[0][n-1]

if __name__ == '__main__':
    arr = 'ABA'
    print(Solution().dps(arr))