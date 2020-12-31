class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n_len = len(prices)
        if n_len < 2:
            return 0
        dp = [[0, 0] for i in range(n_len)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n_len):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])

        return dp[n_len - 1][0]

    # 作者：yong - cai - gu - zi - xi
    # 链接：https: // leetcode - cn.com / problems / best - time - to - buy - and -sell - stock / solution / mei - ban - gu - piao - wen - ti - tong - jie - fan - yi - by - yong - cai /
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # https://leetcode-cn.com/circle/article/qiAgHn/
