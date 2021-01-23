import collections
class Solution(object):
    def __init__(self):
        self.edges = collections.defaultdict(list)
        self.seen = set()

    def dfs(self, index):
        self.seen.add(index)
        for item in self.edges[index]:
            if item not in self.seen:
                self.dfs(item)

    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) < n-1:
            return -1

        for [p, q] in connections:
            self.edges[p].append(q)
            self.edges[q].append(p)

        clique_num = 0
        for i in range(n):
            if i not in self.seen:
                self.dfs(i)
                clique_num += 1
        return clique_num - 1

if __name__ == '__main__':
    n = 6
    connections = [[0,1],[0,2],[0,3],[1,2]]
    print(Solution().makeConnected(n, connections))
