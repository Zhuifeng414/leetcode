class Solution(object):
    def __init__(self):
        return

    def process(self, n, res):
        if n == 0:
            return res
        if n < 0:
            return -1
        return res * max(self.process(n - 2, res) * 2, self.process(n - 3, res) * 3)

    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        return self.process(n, 1)

    def dps(self, n):
        if n == 2:
            return 1
        if n == 3:
            return 2

        dp = [0 for i in range(n+1)]
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n+1):
            dp[i] = max(dp[i-2]*2, dp[i-3]*3)

        return dp[n]

if __name__ == '__main__':
    n = 10
    #print(Solution().cuttingRope(n))
    print(Solution().dps(n))