class Solution(object):
    def __init__(self):
        return

    def process(self, n, index):
        if n <= 0:
            return 0
        if index == n:
            return 1
        if index > n:
            return 0
        return self.process(n, index+1) + self.process(n, index+2)

    def dps(self, n):
        dp = [0 for i in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]

if __name__ == '__main__':
    n = 6
    print(Solution().process(n, 0))
    print('==========================>')
    print(Solution().dps(n))