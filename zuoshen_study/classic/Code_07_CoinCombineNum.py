class Solution(object):
    def __init__(self):
        return

    def process_coin(self, arr, aim, index, sum_res):
        if sum_res == aim:
            return 1
        if index >= len(arr):
            return 0
        if sum_res > aim:
            return 0
        return self.process_coin(arr, aim, index+1, sum_res) \
            + self.process_coin(arr, aim, index+1, sum_res+arr[index])

    def dps_coin(self, arr, aim):
        if len(arr) == 0:
            return 0
        if aim == 0:
            return 1
        n = len(arr)
        dp = [[0 for i in range(aim+1)] for j in range(n)]
        for i in range(n):
            dp[i][0] = 1
            if arr[i] <= aim:
                dp[i][arr[i]] = 1
        # for item in dp:
        #     print(item)
        # print('==================>>>>')
        for i in range(n-2, -1, -1):
            for j in range(1, aim+1):
                # use and not use
                dp[i][j] = dp[i+1][j] + (dp[i+1][j-arr[i]] if j-arr[i] >= 0 else 0)
        # for item in dp:
        #     print(item)
        return dp

    def process_paper(self, arr, aim, index, sum_res):
        #print('now:', index, sum_res)
        if sum_res == aim:
            return 1
        if index >= len(arr):
            return 0
        if sum_res > aim:
            return 0
        num = (aim - sum_res) // arr[index]
        res = 0
        for i in range(num+1):
            res += self.process_paper(arr, aim, index+1, sum_res+arr[index]*i)
        #print('index', index, 'sum_res', sum_res, 'ans', res)
        return res

    def dps_paper(self, arr, aim):
        if len(arr) == 0:
            return  0
        if aim == 0:
            return 1
        n = len(arr)
        dp = [[0 for i in range(aim+1)] for j in range(n)]
        for i in range(n):
            num = aim // arr[i]
            for j in range(num+1):
                dp[i][arr[i]*j] = 1

        for i in range(n-2, -1, -1):
            for j in range(1, aim+1):
                dp[i][j] = dp[i+1][j]
                # 斜率优化 用邻近元素代替枚举行为
                dp[i][j] += (dp[i][j-arr[i]] if j-arr[i]>=0 else 0)
                # num = j // arr[i]
                # sub_res = 0
                # for k in range(num+1):
                #     if j - arr[i]*k >= 0:
                #         sub_res += dp[i+1][j-arr[i]*k]
                # dp[i][j] = sub_res
        for item in dp:
            print(item)
        return dp

    def money_way(self, aim, coin_arr, paper_arr):
        if aim < 0:
            return 0
        if len(coin_arr) == 0 or len(paper_arr) == 0:
            return (1 if aim == 0 else 0)
        dp_coin = self.dps_coin(coin_arr, aim)
        dp_paper = self.dps_paper(paper_arr, aim)
        if len(dp_coin) == 0:
            return dp_paper[0][aim]
        if len(dp_paper) == 0:
            return dp_coin[0][aim]
        print('=============>>>>')
        print('dp_coin', dp_coin[0])
        print('dp_paper', dp_paper[0])
        res = 0
        for coin_money in range(0, aim+1):
            paper_money = aim - coin_money
            res += dp_coin[0][coin_money] * dp_paper[0][paper_money]
        return res

if __name__ == '__main__':
    # coin_arr = [1, 2, 3, 5]
    # aim = 6
    # print(Solution().process_coin(coin_arr, aim, 0, 0))
    # print('=======================>')
    # print(Solution().dps_coin(coin_arr, aim))
    # paper_arr = [1, 2, 5]
    # aim = 3
    # print(Solution().process_paper(paper_arr, aim, 0, 0))
    # print('=======================>')
    # print(Solution().dps_paper(paper_arr, aim))


    coin_arr = [1, 3, 5]
    paper_arr = [1, 2, 5]
    aim = 5
    print(Solution().money_way(aim, coin_arr, paper_arr))