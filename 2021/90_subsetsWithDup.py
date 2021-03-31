class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        tmp = []
        def dfs(nums, index):
            res.append(tmp.copy())
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                else:
                    tmp.append(nums[i])
                    dfs(nums, i+1)
                    tmp.pop()
            return
        dfs(nums, 0)
        return res

if __name__ == '__main__':
    nums = [1, 1]
    print(Solution().subsetsWithDup(nums))