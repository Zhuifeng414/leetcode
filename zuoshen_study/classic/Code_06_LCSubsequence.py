class Solution(object):
    def __init__(self):
        return

    def dps(self, str1, str2):
        dp = [[0 for i in range(len(str2))] for j in range(len(str1))]

        flag = 0
        sub1 = str1[0]
        for i in range(len(str2)):
            sub2 = str2[i]
            if (sub1 == sub2) or (flag == 1):
                dp[0][i] = 1
                flag = 1

        flag = 0
        sub2 = str2[0]

        for i in range(len(str1)):
            sub1 = str1[i]
            if (sub1 == sub2) or (flag == 1):
                dp[i][0] = 1
                flag = 1

        for i in range(1, len(str1)):
            for j in range(1, len(str2)):
                p1 = dp[i-1][j]
                p2 = dp[i][j-1]
                p3 = dp[i-1][j-1] + (1 if str1[i] == str2[j] else 0)
                dp[i][j] = max(max(p1, p2), p3)

        #print(dp)
        return dp[len(str1)-1][len(str2)-1]

    def dps_zip(self, str1, str2):
        dp_up = [0 for i in range(len(str2))]

        flag = 0
        sub1 = str1[0]
        for i in range(len(str2)):
            sub2 = str2[i]
            if (sub1 == sub2) or (flag == 1):
                dp_up[i] = 1
                flag = 1

        flag = 0
        sub2 = str2[0]
        for i in range(1, len(str1)):
            dp_down = [0 for i in range(len(str2))]
            sub1 = str1[i]
            if (sub1 == sub2) or (flag == 1):
                dp_down[0] = 1
            else:
                dp_down[0] = 0
            for j in range(1, len(str2)):
                p1 = dp_up[j]
                p2 = dp_up[j-1] + (1 if str1[i] == str2[j] else 0)
                p3 = dp_down[i-1]
                dp_down[j] = max(max(p1, p2), p3)
            dp_up = dp_down

        #print(dp_down)
        return dp_down[len(str2)-1]





if __name__ == '__main__':
    # str1 = 'wang432'
    str1 = 'teslawang414'
    str2 = str1[::-1]

    print(Solution().dps(str1, str2))
    print('=======================>')
    print(Solution().dps_zip(str1, str2))