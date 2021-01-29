# 并查集模板
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.n = n
        self.setCount = n

    def findset(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1

    def connected(self, x, y):
        x, y = self.findset(x), self.findset(y)
        return x == y

class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m, n = len(heights), len(heights[0])
        edges = list()
        for i in range(m):
            for j in range(n):
                index = i * n + j
                if i > 0:
                    edges.append((index - n, index, abs(heights[i][j] - heights[i - 1][j])))
                if j > 0:
                    edges.append((index - 1, index, abs(heights[i][j] - heights[i][j - 1])))

        edges.sort(key=lambda x:x[2])
        uf = UnionFind(m * n)
        ans = 0
        for x, y, v in edges:
            uf.union(x, y)
            if uf.connected(0, m * n - 1):
                ans = v
                break
        return ans


if __name__ == '__main__':
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    print(Solution().minimumEffortPath(heights))