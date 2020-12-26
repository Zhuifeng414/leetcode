class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        nums.sort()
        max_delta = 0
        for i in range(0, len(nums)-1):
            max_delta = nums[i+1] - nums[i] if nums[i+1] - nums[i] > max_delta else max_delta
        return max_delta
