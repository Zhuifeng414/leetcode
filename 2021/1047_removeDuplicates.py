class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stk = []
        for ch in S:
            if stk and stk[-1] == ch:
                stk.pop()
            else:
                stk.append(ch)
        return ''.join(stk)

if __name__ == '__main__':
    S = "abbaca"
    print(Solution().removeDuplicates(S))