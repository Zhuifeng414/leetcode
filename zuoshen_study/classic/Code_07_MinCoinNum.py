class Solution(object):
    def __init__(self):
        return

    def process(self, arr, aim, index, sum_res, coin_num, res_list):
        if aim == sum_res:
            return res_list.append(coin_num)
        if index >= len(arr):
            return res_list
        if sum_res > aim:
            return res_list
        num = (aim - sum_res) // arr[index]
        for i in range(num+1):
            self.process(arr, aim, index+1, sum_res+i*arr[index], coin_num+i, res_list)
        return res_list

    def process_simple(self, arr, aim, index, sum_res, coin_num, min_res):
        if aim == sum_res:
            return min(coin_num, min_res)
        if index >= len(arr):
            return 1e6
        if sum_res > aim:
            return 1e6
        num = (aim - sum_res) // arr[index]
        for i in range(num+1):
            sub_res = self.process_simple(arr, aim, index+1, sum_res+i*arr[index], coin_num+i, min_res)
            min_res = min(min_res, sub_res)
        return min_res

    def dps(self, arr, aim):
        max_v = 1e6
        if len(arr) == 0 or aim < 0:
            return 0
        if aim == 0:
            return 1
        n = len(arr)
        dp = [[max_v for i in range(aim+1)] for j in range(n)]
        for i in range(n):
            dp[i][0] = 1
            if arr[i] <= aim:
                num = aim // arr[i]
                for j in range(num+1):
                    dp[i][arr[i]*j] = j

        for i in range(1, n):
            for j in range(1, aim+1):
                p1 = dp[i][j]
                p2 = min(dp[i-1][j], ((dp[i][j-arr[i]] + 1) if j-arr[i]>0 else max_v))
                dp[i][j] = min(p1, p2)

        for item in dp:
            print(item)
        return dp[n-1][aim]

if __name__ == '__main__':
    arr = [1, 2, 5]
    aim = 2
    min_res = 1e6
    #res = Solution().process(arr, aim, 0, 0, 0, [])
    print('================================>')
    print(Solution().process_simple(arr, aim, 0, 0, 0, min_res))
    print('================================>')
    print(Solution().dps(arr, aim))

