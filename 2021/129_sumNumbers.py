# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res_list = []
        res = 0
        self.dfs(root, '', res_list)
        for item in res_list:
            #print(item)
            res += int(item)
        return res

    def dfs(self, root, res_str, res_list):
        if root is None:
            res_list.append(res_str)
            return
        sub_res_str = res_str + str(root.val)
        if root.left is not None:
            self.dfs(root.left, sub_res_str, res_list)
        if root.right is not None:
            self.dfs(root.right, sub_res_str, res_list)
        if root.left is None and root.right is None:
            res_list.append(sub_res_str)
        return
