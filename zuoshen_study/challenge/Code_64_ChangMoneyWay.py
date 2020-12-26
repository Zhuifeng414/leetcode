class Solution(object):
    def __init__(self, arr, aim):
        self.arr = arr
        self.aim = aim
        return

    # include and after index, combine amount money of rest
    def process(self, index, rest):
        if rest == 0:
            return 1
        if rest < 0:
            return 0
        if index >= len(self.arr):
            return 0
        num = rest // self.arr[index]
        res = 0
        for i in range(num+1):
            res += self.process(index+1, rest-arr[index]*i)
        return res

    def dps(self):
        if len(self.arr) == 0  or self.aim < 0:
            return 0
        if self.aim == 0:
            return 1
        n = len(self.arr)
        dp = [[0 for i in range(self.aim+1)] for j in range(n)]
        for i in range(n):
            num = self.aim // self.arr[i]
            for j in range(num+1):
                dp[i][j*arr[i]] = 1
        # for item in dp:
        #     print(item)
        for i in range(1, n):
            for j in range(1, aim+1):
                p1 = dp[i][j-arr[i]] if j-arr[i] >= 0 else 0
                p2 = dp[i-1][j]
                dp[i][j] = p1 + p2
        # print('>>>>===================>>>>')
        # for item in dp:
        #     print(item)
        return dp[n-1][aim]

if __name__ == '__main__':
    arr = [1, 2, 5, 7]
    aim = 5
    print(Solution(arr, aim).process(0, aim))
    print('==================>>>>')
    print(Solution(arr, aim).dps())