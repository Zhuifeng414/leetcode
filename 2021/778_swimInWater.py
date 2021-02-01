class UnionFind():
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
        return True

    def connected(self, x, y):
        x, y = self.findset(x), self.findset(y)
        return x == y


class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        edges = list()
        for i in range(n):
            for j in range(n):
                index = i * n + j
                if i > 0:
                    edges.append((index - n, index, max(grid[i][j], grid[i-1][j])))
                if j > 0:
                    edges.append((index - 1, index, max(grid[i][j], grid[i][j-1])))

        edges.sort(key=lambda x:x[2])
        uf = UnionFind(n * n)
        ans = 0
        for x, y, v in edges:
            uf.union(x, y)
            if uf.connected(0, n * n - 1):
                ans = v
                break
        return ans

if __name__ == '__main__':
    grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    print(Solution().swimInWater(grid))

