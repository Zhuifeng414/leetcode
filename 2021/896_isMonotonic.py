class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return True

        if len(A) > 2:
            pd = A[1] - A[0]
            for i in range(2, len(A)):
                if (A[i] - A[i-1]) * pd >= 0:
                    if abs(A[i] - A[i-1]) > abs(pd):
                        pd = A[i] - A[i-1]
                else:
                    return False
        return True