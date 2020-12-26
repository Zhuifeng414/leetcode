class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        return

class IsBSTAndCBT():
    def __init__(self):
        return

    def isBST(self, head):
        if head is None:
            return True
        res = True
        pre = None
        cur1 = head
        cu2 = None
        while cur1 is not None:
            cur2 = cur1.left
            if cur2 is not None:
                while cur2.right is not None and cur2.right is not cur1:
                    cur2 = cur2.right
                if cur2.right is None:
                    cur2.right = cur1
                    cur1 = cur1.left
                else:
                    cur2.right = None
            if pre is None and pre.val > cur1.val:
                res = False
            pre = cur1
            cur1 = cur1.right
        return res

    def isCBT(self, head):
        if head is None:
            return True
        queue = []
        leaf = False
        l, r = None, None
        queue.append(head)
        while len(queue) > 0:
            head = queue.pop()
            l = head.left
            r = head.right
            # 叶节点开启之后，左不为空或者右不为空 False
            # 左为空 右不为空 False
            if (leaf and (l is not None) or (r is not None)) \
                    or ((l is None) and (r is not None)):
                return False
            # 宽度遍历 先加左，再加右
            if l is not None:
                queue.append(l)
            if r is not None:
                queue.append(r)
            if (l is None) or (r is None): # 左为空 并且为空 开启叶子节点阶段
                leaf = True
        return True
