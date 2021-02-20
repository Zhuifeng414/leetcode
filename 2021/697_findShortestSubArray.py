class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res_dict = {}
        #[freq, start, end]
        for i in range(len(nums)):
            item = nums[i]
            if item in res_dict.keys():
                res_dict[item][0] += 1
                res_dict[item][2] = i
            else:
                res_dict[item] = [1, i, i]
        max_freq = 0
        min_len = len(nums)
        for k, v in res_dict.items():
            max_freq = max(max_freq, v[0])
        for k, v in res_dict.items():
            if v[0] == max_freq:
                min_len = min(min_len, v[2]-v[1]+1)
        return min_len