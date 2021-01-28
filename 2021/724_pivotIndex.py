# when index = i, left:sum, right: all_sum - sum - nums[i]
# sum = all_sum - sum - nums[i]
# 2 * sum = all_sum - nums[i]
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        all = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if 2*left_sum == all - nums[i]:
                return i
            else:
                left_sum += nums[i]
        return -1

if __name__ == '__main__':
    nums = [1, 7, 3, 6, 5, 6]
    print(Solution().pivotIndex(nums))



