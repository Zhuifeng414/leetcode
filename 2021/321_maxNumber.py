class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_res = []
        for i in range(k+1):
            if i <= len(nums1) and k-i <= len(nums2):
                new_res = self.merge(self.pick_K(nums1, i), self.pick_K(nums2, k-i))
                if max_res < new_res:
                    max_res = new_res
        return max_res

    def pick_K(self, num, k):
        drop = len(num) - k
        stack = []
        for item in num:
            while stack and drop and stack[-1]<item:
                stack.pop()
                drop -= 1
            stack.append(item)
        return stack[:k]

    def merge(self, list_a, list_b):
        res = []
        while list_a or list_b:
            bigger = list_a if list_a > list_b else list_b
            res.append(bigger.pop(0))
        return res

if __name__ == '__main__':
    nums1 = [6, 7]
    nums2 = [6, 0, 4]
    k = 5
    print(Solution().maxNumber(nums1, nums2, k))