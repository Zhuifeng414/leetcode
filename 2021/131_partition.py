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

if __name__ == '__main__':
    s = 'aab'
    print(Solution().partition(s))



