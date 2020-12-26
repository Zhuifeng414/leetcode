class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        res_len = len(num) - k
        stack = []
        for item in num:
            while (k > 0) and stack and (stack[-1] > item):
                stack.pop()
                k -= 1
            stack.append(item)
        return ''.join(stack[:res_len]).lstrip('0') or '0'

if __name__ == '__main__':
    num = "10"
    k = 2
    print(Solution().removeKdigits(num, k))