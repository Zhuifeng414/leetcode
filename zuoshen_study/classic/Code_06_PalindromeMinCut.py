class Solution(object):
    def __init__(self):
        return

    def dps(self, arr):
        if len(arr) == 0:
            return 0
        str_len = len(arr)
        dp = [0 for i in range(str_len+1)]
        dp[str_len] = -1
        p = [[False for i in range(str_len+1)] for j in range(str_len+1)]
        for i in range(str_len-1, -1, -1):
            dp[i] = 1e6
            for j in range(i, str_len):
                if arr[i] == arr[j] and (j-i<2 or p[i+1][j-1]):
                    p[i][j] = True
                    dp[i] = min(dp[i], dp[j+1]+1)
        return dp[0]

if __name__ == '__main__':
    arr = 'wangieleiteslawangg'
    print(Solution().dps(arr))