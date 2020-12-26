class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Info(object):
    def __init__(self, h, g):
        self.h = h
        self.g = g

class Solution(object):
    def process(self, root):
        if root is None:
            return Info(0, 0)

        leftInfo = self.process(root.left)
        rightInfo = self.process(root.right)
        h = max(leftInfo.h, rightInfo.h) + 1
        g = max(max(leftInfo.g, rightInfo.g), leftInfo.h + rightInfo.h + 1)
        return Info(h, g)


    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        res = self.process(root)
        return res.g

    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
res = Solution().diameterOfBinaryTree(root)
print(res)