class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) <= 1:
            return sum(heights)
        heights = [0] + heights + [0]
        stack = [0]
        res = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                max_heights = heights[stack.pop()]
                max_with = i - stack[-1] - 1
                res = max(res, max_heights * max_with)
            stack.append(i)
        return res

if __name__ == '__main__':
    heights = [2, 1, 2]
    print(Solution().largestRectangleArea(heights))
