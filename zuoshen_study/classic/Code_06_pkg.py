import sys
class Solution(object):
    def __init__(self):
        return

    def process(self, arr, index, rest):
        if rest < 0:
            return -1
        if index == len(arr):
            return 1
        next1 = self.process(arr, index+1, rest)
        next2 = self.process(arr, index+1, rest-arr[index])
        return next1 + (next2 if next2 != -1 else 0)

    def dps(self, arr, rest):
        dp = [[0 for i in range(rest+1)] for j in range(len(arr)+1)]

        for i in range(rest+1):
            dp[len(arr)][i] = 1

        for i in range(len(arr)-1, -1, -1):
            for j in range(rest + 1):
                dp[i][j] = dp[i+1][j] + (dp[i+1][j - arr[i]] if j >= arr[i] else 0)
        return dp[0][rest]

    def dps2(self, arr, rest):
        dp = [[0 for i in range(rest + 1)] for j in range(len(arr))]
        for i in range(len(arr)):
            dp[i][0] = 1

        if arr[0] <= rest:
            dp[0][arr[0]] = 1

        for i in range(1, len(arr)):
            for j in range(rest+1):
                dp[i][j] = dp[i-1][j] + (dp[i-1][j-arr[i]] if j >= arr[i] else 0)
        #print(dp)
        res = 0
        for j in range(rest+1):
            res += dp[len(arr)-1][j]
        return res

    def dps_zip(self, arr, rest):

        dp_down = [0 for i in range(rest+1)]
        dp_up = [0 for i in range(rest+1)]

        dp_down = [1 for i in range(rest + 1)]

        for i in range(len(arr)-1, -1, -1):
            dp_up = [0 for i in range(rest + 1)]
            for j in range(rest + 1):
                dp_up[j] = dp_down[j] + (dp_down[j-arr[i]] if j>=arr[i] else 0)
                #dp[i][j] = dp[i+1][j] + (dp[i+1][j - arr[i]] if j >= arr[i] else 0)
            dp_down = dp_up
        return dp_up[rest]

    def test1(self):
        par1 = sys.stdin.readline().strip().split()
        n, rest = int(par1[0]), int(par1[1])
        par2 = sys.stdin.readline().strip().split()
        arr = [int(item) for item in par2]
        print(Solution().process(arr, 0, rest))

if __name__ == "__main__":

    arr = [1, 3, 4, 5]
    rest = 5
    #print(Solution().dps(arr, rest))
    print(Solution().dps_zip(arr, rest))



