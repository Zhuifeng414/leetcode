class Solution(object):
    def dp_process(self, arr):
        dp = [[0 for i in range(len(arr[0]))] for j in range(len(arr))]
        m = len(arr)
        n = len(arr[0])
        for i in range(n):
            dp[m-1][i] = arr[m-1][i]
        for i in range(n-2, -1, -1):
            for j in range(n):
                sub_seq = dp[i+1][:j] + dp[i+1][j+1:]
                pre_min = min(sub_seq)
                dp[i][j] = pre_min + arr[i][j]
        return dp

    def minFallingPathSum(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """
        if len(arr) == 0 or len(arr[0]) == 0:
            return 0
        dp = self.dp_process(arr)
        #print(dp)
        return min(dp[0])

arr = [[1,2,3],[4,5,6],[7,8,9]]
res = Solution().minFallingPathSum(arr)
print(res)


# 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
#
# 你需要按照以下要求，帮助老师给这些孩子分发糖果：
#
# 每个孩子至少分配到 1 个糖果。
# 相邻的孩子中，评分高的孩子必须获得更多的糖果。
# 那么这样下来，老师至少需要准备多少颗糖果呢？
#
# 示例 1:
#
# 输入: [1,0,2]
# 输出: 5
# 解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
# 示例 2:
#
# 输入: [1,2,2]
# 输出: 4
# 解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
#      第三个孩子只得到 1 颗糖果，这已满足上述两个条件。