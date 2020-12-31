# https://leetcode-cn.com/problems/patching-array/

class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        x = 1
        index = 0
        res = 0

        while x <= n:
            if (index < len(nums)) and (nums[index] <= x):
                x += nums[index]
                index += 1
            else:
                x = 2 * x
                res += 1
        return res
