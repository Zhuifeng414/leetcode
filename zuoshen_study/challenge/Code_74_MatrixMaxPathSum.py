class Solution(object):
    def __init__(self):
        return

    def print_df(self, dp):
        for item in dp:
            print(item)

    def dps(self, mat):
        if len(mat) == 0 or len(mat[0]) == 0:
            return 0
        n = len(mat)
        m = len(mat[0])
        dp = [[0 for i in range(m)] for j in range(n)]
        dp[n-1][m-1] = 1 if (mat[n-1][m-1] > 0) else (1 - mat[n-1][m-1])
        for i in range(m-2, -1, -1):
            dp[n-1][i] = max(dp[n-1][i+1] - mat[n-1][i], 1)
        self.print_df(dp)
        for i in range(n-2, -1, -1):
            dp[i][m-1] = max(dp[i+1][m-1] - mat[i][m-1], 1)
            for j in range(m-2, -1, -1):
                p1 = max(dp[i][j+1] - mat[i][j], 1)
                p2 = max(dp[i+1][j] - mat[i][j], 1)
                dp[i][j] = min(p1, p2)
        print('>>>=================>>>')
        self.print_df(dp)
        return dp

if __name__ == '__main__':
    mat = [
        [-2, -3, 3],
        [-5, -10, 1],
        [0, 30, -5]
    ]
    # res = Solution().process(mat, 2, 2, 0)
    # print(res)
    dp = Solution().dps(mat)
