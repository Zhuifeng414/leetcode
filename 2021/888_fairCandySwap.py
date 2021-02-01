class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        # sa - a + b = sb - b + a
        # a = (sa - sb)/2 + b
        sum_A = sum(A)
        sum_B = sum(B)
        delta = (sum_A - sum_B) / 2
        set_A = set(A)
        for item in B:
            if (item + delta) in set_A:
                return [item + delta, item]
