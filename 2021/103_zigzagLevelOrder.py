# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        stack = [root]
        res = []
        status = 0
        while stack:
            sub_res = []
            buff = []
            for sub_root in stack:
                sub_res.append(sub_root.val)
                if sub_root.left:
                    buff.append(sub_root.left)
                if sub_root.right:
                    buff.append(sub_root.right)
            stack = buff
            if status == 0:  # 下一次从右往左
                res.append(sub_res)
                status = 1
            elif status == 1:  # 下一次从左往右
                res.append(sub_res[::-1])
                status = 0
        return res

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().zigzagLevelOrder(root))






