class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def process(self, root, cum):
        if root is None:
            return cum
        cum = self.process(root.right, cum)
        cum = root.val + cum
        root.val = cum
        #print(cum)
        cum = self.process(root.left, cum)
        return cum

    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        cum = 0
        self.process(root, cum)
        return root


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
res = Solution().bstToGst(root)
print(res)



