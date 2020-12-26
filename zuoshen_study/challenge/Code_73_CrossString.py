class Solution(object):
    def __init__(self):
        return

    def dps(self, sa, sb, aim):
        if len(aim) != len(sa) + len(sb):
            return 0
        n = len(sa)
        m = len(sb)
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            if sa[i-1] == aim[i-1] and dp[i-1][0] == 1:
                dp[i][0] = 1
            else:
                dp[i][0] = 0
        for i in range(1, m+1):
            if sb[i-1] == aim[i-1] and dp[0][i-1] == 1:
                dp[0][i] = 1
            else:
                dp[0][i] = 0
        # for item in dp:
        #     print(item)
        for i in range(1, n+1):
            for j in range(1, m+1):
                p1 = 1 if (aim[i+j-1] == sa[i-1] and dp[i-1][j] == 1) else 0
                p2 = 1 if (aim[i+j-1] == sb[j-1] and dp[i][j-1] == 1) else 0
                dp[i][j] = max(p1, p2)
        # print('=============>')
        # for item in dp:
        #     print(item)
        return dp

    def dps_zip(self, sa, sb, aim):
        if len(aim) != len(sa) + len(sb):
            return 0

        n = len(sa)
        m = len(sb)

        dp = [0 for i in range(m+1)]
        dp[0] = 1
        for i in range(1, m+1):
            if sb[i-1] == aim[i-1] and dp[i-1] == 1:
                dp[i] = 1
            else:
                dp[i] = 0
        print(0, dp)
        for i in range(1, n+1):
            dp[0] = 1 if (dp[0] == 1 and sa[i-1] == aim[i-1]) else 0
            for j in range(1, m+1):
                tmp = dp[j]
                p1 = 1 if (dp[j-1] == 1 and aim[i+j-1] == sb[j-1]) else 0
                p2 = 1 if (tmp == 1 and aim[i+j-1] == sa[i-1]) else 0
                dp[j] = max(p1, p2)
            print(i, dp)
        return dp

if __name__ == '__main__':
    sa = 'wang41'
    sb = 'tesl4'
    aim = 'teslwang414'
    dp = Solution().dps(sa, sb, aim)
    for item in dp:
        print(item)
    print('>>>===============>>>>')
    dp_zip = Solution().dps_zip(sa, sb, aim)