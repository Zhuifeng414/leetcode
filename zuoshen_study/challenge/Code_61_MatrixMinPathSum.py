class Solution(object):
    def __init__(self):
        return

    def process(self, m, x, y, psum):
        if x == len(m)-1 and y == len(m[0])-1:
            return psum+m[x][y]
        # if at the end, can only move to right
        if x == len(m)-1:
            return self.process(m, x, y+1, psum+m[x][y])
        # if at the right, can only move down
        if y == len(m[0])-1:
            return self.process(m, x+1, y, psum+m[x][y])
        return min(self.process(m, x, y+1, psum+m[x][y]), self.process(m, x+1, y, psum+m[x][y]))

    def dps(self, m):
        if len(m) == 0 or len(m[0]) == 0:
            return 0
        row = len(m)
        col = len(m[0])
        dp = [[0 for i in range(col)] for j in range(row)]
        dp[0][0] = m[0][0]
        for i in range(1, col):
            dp[0][i] = dp[0][i-1] + m[0][i]
        for i in range(1, row):
            dp[i][0] = dp[i-1][0] + m[i][0]
        # for item in dp:
        #     print(item)
        # print('>>>>>==================>>>>>')
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])+ m[i][j]
        #
        # for item in dp:
        #     print(item)
        return dp[row-1][col-1]



if __name__ == '__main__':
    m = [
        [1, 3, 5, 9],
        [8, 1, 3, 4],
        [5, 0, 6, 1],
        [8, 8, 4, 0]
    ]
    print(Solution().process(m, 0, 0, 0))
    print('==========================>')
    print(Solution().dps(m))