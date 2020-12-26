# 给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
# # # 区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。
# # #
# # # 说明:
# # # 最直观的算法复杂度是 O(n2) ，请在此基础上优化你的算法。
# # #
# # # 示例:
# # #
# # # 输入: nums = [-2,5,-1], lower = -2, upper = 2,
# # # 输出: 3
# # # 解释: 3个区间分别是: [0,0], [2,2], [0,2]，它们表示的和分别为: -2, -1, 2。

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        t = [0 for i in range(len(nums))]
        t[0] = nums[0]
        for i in range(1, len(nums)):
            t[i] = t[i-1] + nums[i]
        L = 0
        R = 0
        res = 0
        while L < len(nums):
            for R in range(L, len(nums)):
                if lower <= t[R] - t[L] + nums[L] <= upper:
                    res += 1


