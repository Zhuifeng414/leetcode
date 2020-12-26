class Solution(object):
    def __init__(self, ic, dc, rc):
        self.ic = ic
        self.dc = dc
        self.rc = rc
        return

    # sa --> sb
    def dps(self, sa, sb):
        if len(sa) == 0:
            return self.ic * len(sb)
        if len(sb) == 0:
            return self.dc * len(sa)
        n = len(sa)
        m = len(sb)
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(n+1):
            dp[i][0] = self.dc * i
        for i in range(m+1):
            dp[0][i] = self.ic * i

        # for item in dp:
        #     print(item)

        for i in range(1, n+1):
            for j in range(1, m+1):
                p1 = dp[i-1][j] + self.dc
                p2 = dp[i][j-1] + self.ic
                p3 = dp[i-1][j-1] + (0 if sa[i-1] == sb[j-1] else self.rc)
                dp[i][j] = min(min(p1, p2), p3)
        # print('===========>>>')
        # for item in dp:
        #     print(item)
        return dp

    def dps_zip(self, sa, sb):
        if len(sa) == 0:
            return self.ic * len(sb)
        if len(sb) == 0:
            return self.dc * len(sa)

        n = len(sa)
        m = len(sb)

        dp = [i*self.ic for i in range(m+1)]
        print(0, dp)
        for i in range(1, n+1):
            leftUp = dp[0]
            dp[0] = self.dc * i
            for j in range(1, m+1):
                tmp = dp[j]
                p1 = tmp + self.dc
                p2 = dp[j-1] + self.ic
                p3 = leftUp + (0 if sa[i-1] == sb[j-1] else self.rc)
                dp[j] = min(min(p1, p2), p3)
                leftUp = tmp
            print(i, dp)
        return dp



if __name__ == '__main__':
    sa = 'wagt'
    sb = 'tesg'
    ic = 1
    dc = 2
    rc = 3
    dp1 = Solution(ic, dc, rc).dps(sa, sb)
    dp2 = Solution(ic, dc, rc).dps_zip(sa, sb)
    print('==============>>>')
    for item in dp1:
        print(item)
    print('==============>>>')
    #print(dp2)