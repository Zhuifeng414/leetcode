class Solution:
    def findCheapestPrice_ans(self, n: int, flights, src, dst, K):
        dp = [float('inf') for _ in range(n)]
        dp[src] = 0
        for i in range(K+1):
            tmp = dp[:]
            for u, v, w in flights:
                dp[v] = min(dp[v],tmp[u]+w)
        return dp[dst] if dp[dst] != float('inf') else -1

    def findCheapestPrice_ans(self, n: int, flights, src, dst, K):
        dp = [float('inf') for i in range(n)]
        dp[src] = 0
        for i in range(K+1):
            tmp = dp[:]
            for u, v, w in flights:
                dp[v] = min(dp[v], tmp[u] + w)
        return dp[dst] if dp[dst] != float('inf') else -1

if __name__ == '__main__':
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    print(Solution().findCheapestPrice_ans(n, flights, src, dst, k))

