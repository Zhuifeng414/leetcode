class Solution(object):
    def __init__(self):
        return

    # edict str1 to str2
    def dps_mincost(self, str1, str2, ic, dc, rc):
        if len(str1) == 0 or len(str2) == 0:
            return 0
        row = len(str1) + 1
        col = len(str2) + 1
        dp = [[0 for j in range(col)] for i in range(row)]
        # only delete
        for i in range(row):
            dp[i][0] = dc * i
        # only add
        for i in range(col):
            dp[0][i] = ic * i
        for i in range(1, row):
            for j in range(1, col):
                if str1[i-1] == str2[j-1]:
                    p1 = dp[i-1][j-1]
                else:
                    p1 = dp[i-1][j-1] + rc
                p2 = dp[i-1][j] + dc
                p3 = dp[i][j-1] + ic
                dp[i][j] = min(min(p1, p2), p3)
        return dp[row-1][col-1]


    # edict str1 to str2
    def dps_mincost_zip(self, str1, str2, ic, dc, rc):
        if len(str1) == 0 or len(str2) == 0:
            return 0
        # when str2 longer, switch str1 str2 and ic dc
        # to confirm str2 is shorter and space is smaller
        if len(str2) > len(str1):
            str1, str2 = str2, str1
            ic, dc = dc, ic

        row = len(str1) + 1
        col = len(str2) + 1
        dp = [0 for i in range(col)]
        # only add
        for i in range(col):
            dp[i] = ic * i
        for i in range(1, row):
            tmp_up_left = dp[0]
            dp[0] = dc * i # only delete
            for j in range(1, col):
                tmp_up = dp[j]
                if str1[i-1] == str2[j-1]:
                    p1 = tmp_up_left
                else:
                    p1 = tmp_up_left + rc
                p2 = tmp_up + dc
                p3 = dp[j-1] + ic
                dp[j] = min(min(p1, p2), p3)

                tmp_up_left = tmp_up # very nice !!
        return dp[col-1]

if __name__ == '__main__':
    str1 = 'wan'
    str2 = 'wal4'
    ic = 1
    dc = 2
    rc = 3
    print(Solution().dps_mincost(str1, str2, ic, dc, rc))
    print('================================>')
    print(Solution().dps_mincost_zip(str1, str2, ic, dc, rc))