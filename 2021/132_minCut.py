class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        dp = [[True for i in range(n)] for j in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = (s[i] == s[j]) & (dp[i+1][j-1])

        #print(dp)

        ans = []
        res = []

        def dfs(index):
            if index >= n:
                res.append(ans[:])
                #print(res)
                return

            for j in range(index, n):
                if dp[index][j]:
                    ans.append(s[index:j+1])
                    dfs(j+1)
                    ans.pop()

        dfs(0)
        return res

    def minCut_init(self, s):
        """
        :type s: str
        :rtype: int
        """
        cut_res = self.partition(s)
        min_cut = len(s)-1
        for item in cut_res:
            min_cut = min(len(item)-1, min_cut)
        return min_cut

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[True for i in range(n)] for j in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = (s[i] == s[j]) & (dp[i + 1][j - 1])

        f = [len(s)-1 for i in range(len(s))]
        for i in range(n):
            if dp[0][i]:
                f[i] = 0
            else:
                for j in range(i):
                    if dp[j+1][i]:
                        f[i] = min(f[i], f[j] + 1)
        return f[len(s)-1]



if __name__ == '__main__':
    s = 'aab'
    print(Solution().minCut(s))



