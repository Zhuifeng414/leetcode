class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bc = {}
        for item in nums:
            if item in bc.keys():
                bc[item] += 1
            else:
                bc[item] = 1

        res = 0
        for k in bc.keys():
            if bc[k] > 1:
                res += bc[k] * (bc[k] - 1) >> 1
        return res

nums = [1]
res = Solution().numIdenticalPairs(nums)
print(res)