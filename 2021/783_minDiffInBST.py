# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_val = 1e6
        pre_val = 1e6
        if root is not None:
            stack = []
            while stack or root is not None:
                if root is not None:
                    stack.append(root)
                    root = root.left
                else:
                    root = stack.pop()
                    min_val = min(min_val, abs(root.val - pre_val))
                    pre_val = root.val
                    root = root.right
        return min_val


