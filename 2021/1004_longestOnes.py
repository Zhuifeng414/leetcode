# https://leetcode-cn.com/problems/max-consecutive-ones-iii/

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        pl, pr = 0, 0
        zeros = 0
        res = 0
        while pr < len(A):
            if A[pr] == 0:
                zeros += 1
            while zeros > K:
                if A[pl] == 0:
                    zeros -= 1
                pl += 1
            res = max(pr - pl + 1, res)
            pr += 1
        return res