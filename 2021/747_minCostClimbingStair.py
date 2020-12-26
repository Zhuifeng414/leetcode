class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) <= 1:
            return sum(cost)
        return min(self.dfs(cost, 0, 0), self.dfs(cost, 1, 0))


    def dfs(self, cost, index, fee):
        ## 数据量大的时候会超时
        if index >= len(cost):
            return fee
        return min(self.dfs(cost, index+1, fee+cost[index]), self.dfs(cost, index+2, fee+cost[index]))

    def dp_solve(self, cost):
        if len(cost) <= 1:
            return sum(cost)
        if len(cost) == 2:
            return min(cost)
        dp = [0 for item in cost]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[-1], dp[-2])

if __name__ == '__main__':
    check_list = [
        [[10, 15, 20], 15],
        [[1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6]
    ]
    index = 0
    for [cost, ans] in check_list:
        res = Solution().dp_solve(cost)
        if res == ans:
            print('yes:', index)
        else:
            print('error:', index, 'ans:', ans, 'yours:', res)
