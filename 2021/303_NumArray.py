class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum_nums = [0] * len(nums)
        pre_sum = 0
        for i in range(len(nums)):
            self.sum_nums[i] = pre_sum + nums[i]
            pre_sum = self.sum_nums[i]
        return

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum_nums[j] - (self.sum_nums[i-1] if i >= 1 else 0)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)