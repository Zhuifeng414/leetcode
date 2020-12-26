class Solution(object):
    def __init__(self):
        return

    def dps(self, sa, sb):
        if len(sa) == 0 or len(sb) == 0:
            return 0
        dp = [[0 for i in range(len(sb))] for j in range(len(sa))]
        for i in range(len(sa)):
            dp[i][0] = (1 if sb[0] == sa[i] else 0)
        for i in range(len(sb)):
            dp[0][i] = (1 if sa[0] == sb[i] else 0)
        # for item in dp:
        #     print(item)
        for i in range(1, len(sa)):
            for j in range(1, len(sb)):
                p1 = dp[i-1][j]
                p2 = dp[i][j-1]
                p3 = dp[i-1][j-1] + (1 if sa[i] == sb[j] else 0)
                dp[i][j] = max(max(p1, p2), p3)
        # print('=============>>>>')
        # for item in dp:
        #     print(item)
        return dp

    def dp2LCSequence(self, dp, sa, sb):
        i = len(sa)-1
        j = len(sb)-1
        res = ''
        while i >= 0 and j >= 0:
            if dp[i][j] == dp[i-1][j]:
                i -= 1
            elif dp[i][j] == dp[i][j-1]:
                j -= 1
            elif dp[i][j] == dp[i-1][j-1] + 1:
                res += sa[i]
                #print(i, sa[i], res)
                i -= 1
                j -= 1
            else:
                i -= 1
                j -= 1
        if i >= 0:
            res += sa[i]
        if j >= 0:
            res += sb[j]
        return res[::-1]

if __name__ == '__main__':
    sa = 'wang414'
    sb = 'tsl45wag4'
    dp = Solution().dps(sa, sb)
    print('=============>>>>')
    for item in dp:
        print(item)
    print('=============>>>>')
    print(Solution().dp2LCSequence(dp, sa, sb))