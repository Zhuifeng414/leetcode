
# 作者：dangerusswilson
# 链接：https: // leetcode - cn.com / problems / path -
# with-maximum - probability / solution / python - bfs - dijkstra - by - dangerusswilson /
#     来源：力扣（LeetCode）
#     著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        import heapq
        import collections
        import math
        dic = collections.defaultdict(dict)
        for i, edge in enumerate(edges):
            print(i, edge)
            a, b = edge
            dic[a][b] = succProb[i]
            dic[b][a] = succProb[i]
        q = [(0, start)]
        seen = set()
        while q:
            prob, node = heapq.heappop(q)
            if node == end: return math.exp(-prob)
            seen.add(node)
            for nxt in dic[node]:
                if nxt not in seen:
                    heapq.heappush(q, (prob - math.log(dic[node][nxt]), nxt))
        return 0

n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2

res = Solution().maxProbability(n, edges, succProb, start, end)
print(res)
