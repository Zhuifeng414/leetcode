class Solutionn(object):
    def __init__(self):
        return

    def process(self, m, i, j):
        # 最左侧
        if j == 0:
            return [m[i][j], -m[i][j]] # [未使用过， 使用过]
        # 左侧的格子
        preAns = self.process(m, i, j-1)
        preUnuse = preAns[0]
        preUse = preAns[1]
        # 有上方的格子
        if i-1 >= 0:
            preAns = self.process(m, i-1, j-1)
            preUnuse = max(preUnuse, preAns[0])
            preUse = max(preUse, preAns[1])
        # 有下方的格子
        if i+1 < len(m):
            preAns = self.process(m, i+1, j-1)
            preUnuse = max(preUnuse, preAns[0])
            preUse = max(preUse, preAns[1])

        no = -1
        yes = -1
        # 如果之前没有使用
        if preUnuse >= 0:
            # 这次也不使用
            no = preUnuse + m[i][j]
            # 这次使用
            yes = preUnuse - m[i][j]
        # 之前有使用
        if preUse >= 0:
            # 这次不能使用
            yes = max(yes, preUse + m[i][j])
        return [no, yes]

    def game(self, m):
        if len(m) == 0 or len(m[0]) == 0:
            return 0
        max_res = -999999
        for i in range(len(m)):
            for j in range(len(m[0])):
                ans = self.process(m, i, j)
                max_res = max(max_res, max(ans[0], ans[1]))
        return max_res

    def dps(self, m):
        if len(m) == 0 or len(m[0]) == 0:
            return 0
        max_res = -99999999
        dp = [[[-99999999, -99999999] for i in range(len(m[0]))] for j in range(len(m))]
        for i in range(len(dp)):
            dp[i][0][0] = m[i][0] # unuse
            dp[i][0][1] = -m[i][0] # use
            max_res = max(dp[i][0][0], dp[i][0][1])

        for i in range(len(m)):
            for j in range(1, len(m[0])):
                preUnuse = dp[i][j-1][0]
                preUse = dp[i][j-1][1]
                if i-1 >= 0:
                    preUnuse = max(preUnuse, dp[i-1][j-1][0])
                    preUse = max(preUse, dp[i-1][j-1][1])
                if i+1 < len(m):
                    preUnuse = max(preUnuse, dp[i+1][j-1][0])
                    preUse = max(preUse, dp[i+1][j-1][1])
                dp[i][j][0] = -1
                dp[i][j][1] = -1
                if preUnuse >= 0:
                    dp[i][j][0] = m[i][j] + preUnuse #之前不用 这次也不用
                    dp[i][j][1] = -m[i][j] + preUnuse #之前不用 这次用

                if preUse >= 0:
                    # |之前不用 这次用| 和 |之前用 这次不用| 取最大
                    dp[i][j][1] = max(dp[i][j][1], m[i][j] + preUse)
                max_res = max(max_res, max(dp[i][j][0], dp[i][j][1]))
            for item in dp:
                print(item)
        return max_res

if __name__ == '__main__':
    matrix = [
        [-100, -4000, -10000],
        [-200, -2000, -100000],
        [-300, -1000, -60000],
        [-2000, -5000, -200000]
    ]

    print(Solutionn().game(matrix))
    print('========================>')
    print(Solutionn().dps(matrix))