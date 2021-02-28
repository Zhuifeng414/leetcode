class Solution(object):

    def dfs(self, s, l, r, k):
        import collections
        wf = collections.Counter()
        for i in range(l, r):
            wf[ord(s[i]) - ord('a')] += 1

        for i in range(l, r):
            if wf[ord(s[i]) - ord('a')] < k:
                return max(self.dfs(s, l, i, k), self.dfs(s, i + 1, r, k))

        return r - l

    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        return self.dfs(s, 0, len(s), k)

    def window_solver(self, s, k):
        import collections
        wf = collections.Counter()
        for i in range(len(s)):
            wf[ord(s[i]) - ord('a')] += 1

        l, r = 0, 0
        less = 0
        res = 0
        while r < len(s):
            wf[ord(s[l])-ord('a')] += 1

            if wf[ord(s[r])-ord('a')] < k:
                less += 1
            if less == 0:
                res = max(res, r-l+1)
            while less > 0 and l <= r:
                if wf[ord(s[l])-ord('a')] < k:
                    less -= 1
                l += 1

            r += 1
        return res

if __name__ == '__main__':
    s = "ababacb"
    k = 3
    print(Solution().window_solver(s, k))