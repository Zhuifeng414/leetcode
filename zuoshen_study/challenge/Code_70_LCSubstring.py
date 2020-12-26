class Solution(object):
    def __init__(self):
        return

    def dps(self, sa, sb):
        if len(sa) == 0 or len(sb) == 0:
            return 0
        n = len(sa)
        m = len(sb)
        dp = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            dp[i][0] = 1 if sb[0] == sa[i] else 0
        for i in range(m):
            dp[0][i] = 1 if sa[0] == sb[i] else 0
        # for item in dp:
        #     print(item)
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = (dp[i-1][j-1] + 1) if sa[i] == sb[j] else 0
        # print('==============>>>>')
        # for item in dp:
        #     print(item)
        return dp

    def dp2LCString(self, dp, sa, sb):
        mv = dp[0][0]
        mi = 0
        mj = 0
        for i in range(len(sa)):
            for j in range(len(sb)):
                if dp[i][j] > mv:
                    mv = dp[i][j]
                    mi = i
                    mj = j
        return sa[mi-mv+1 : mi+1]

if __name__ == '__main__':
    sa = 'wanzhuigt'
    sb = 'wangtesla'
    dp = Solution().dps(sa, sb)
    res = Solution().dp2LCString(dp, sa, sb)
    print(res)