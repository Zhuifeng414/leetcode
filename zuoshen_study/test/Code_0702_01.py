class Node(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        return

    def process(self, L, R):
        if L > R:
            return [None]
        all_trees = []
        for i in range(L, R+1):
            left_trees = self.process(L, i-1)
            right_trees = self.process(i+1, R)
            for l in left_trees:
                for r in right_trees:
                    current_tree = Node(i)
                    current_tree.left = l
                    current_tree.right = r
                    all_trees.append(current_tree)
        return all_trees

    def generate_trees(self, n):
        return self.generate_trees(1, n) if n else []




if __name__ == '__main__':
    res = []
    n = 5
    arr = [i for i in range(1, n+1)]
    L = 0
    R = len(arr) - 1
    res = Solution().process(n, arr, L, R, res)