# Alice 和 Bob 共有一个无向图，其中包含 n 个节点和 3  种类型的边：
#
# 类型 1：只能由 Alice 遍历。
# 类型 2：只能由 Bob 遍历。
# 类型 3：Alice 和 Bob 都可以遍历。
# 给你一个数组 edges ，其中 edges[i] = [typei, ui, vi] 表示节点 ui 和 vi 之间存在类型为 typei 的双向边。请你在保证图仍能够被 Alice和 Bob 完全遍历的前提下，找出可以删除的最大边数。如果从任何节点开始，Alice 和 Bob 都可以到达所有其他节点，则认为图是可以完全遍历的。
#
# 返回可以删除的最大边数，如果 Alice 和 Bob 无法完全遍历图，则返回 -1 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# class UnionFind:
#     def __init__(self, size):
#         self.father = [None] * (size + 1)
#         self.num_of_sets = size
#
#     def find(self, x):
#         if self.father[x] is None: return x
#         self.father[x] = self.find(self.father[x])
#         return self.father[x]
#
#     def is_connected(self, x, y):
#         return self.find(x) == self.find(y)
#
#     def merge(self, x, y):
#         self.father[self.find(x)] = self.find(y)
#         self.num_of_sets -= 1

class UnionFind:
    def __init__(self, size):
        self.father = [None] * (size + 1)
        self.num_of_sets = size

    def find(self, x):
        if self.father[x] is None: return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def merge(self, x, y):
        self.father[self.find(x)] = self.find(y)
        self.num_of_sets -= 1

class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        res = 0
        uf_alice = UnionFind(n)
        uf_bob = UnionFind(n)

        for _type, n1, n2 in edges:
            if _type == 3:
                if not uf_alice.is_connected(n1, n2):
                    uf_alice.merge(n1, n2)
                    uf_bob.merge(n1, n2)
                else:
                    res += 1

        for _type, n1, n2 in edges:
            if _type == 1:
                if not uf_alice.is_connected(n1, n2):
                    uf_alice.merge(n1, n2)
                else:
                    res += 1

            if _type == 2:
                if not uf_bob.is_connected(n1, n2):
                    uf_bob.merge(n1, n2)
                else:
                    res += 1
        return -1 if uf_alice.num_of_sets * uf_bob.num_of_sets > 1 else res

if __name__ == '__main__':
    n = 4
    edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
    print(Solution().maxNumEdgesToRemove(n, edges))
