class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        max_len = 1
        # for i in range(1, len(nums)):
        i = 1
        while i < len(nums):
            sub_max_len = 1
            while (i < len(nums)) and (nums[i - 1] < nums[i]):
                sub_max_len += 1
                i += 1
            i += 1
            max_len = max(max_len, sub_max_len)

        max_len = max(max_len, sub_max_len)
        return max_len

if __name__ == '__main__':
    nums = [2,2,2,2,2]
    print(Solution().findLengthOfLCIS(nums))