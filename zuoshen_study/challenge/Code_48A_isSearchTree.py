class PrintBinaryTree():
    def __init__(self):
        return

    def getSpace(self, num):
        space = " " * num
        return space

    def printInOrder(self, head, height, to, leng):
        if head is None:
            return
        self.printInOrder(head.right, height + 1, 'v', leng)
        val = str(to) + str(head.val) + str(to)
        # print('val', val)
        lenM = len(str(val))
        lenL = int((leng - lenM) / 2)
        lenR = leng - lenM - lenL
        val = self.getSpace(lenL) + val + self.getSpace(lenR)
        print(self.getSpace(height * leng) + val)
        self.printInOrder(head.left, height + 1, '^', leng)

    def printTree(self, head):
        print('Binary Tree')
        self.printInOrder(head, 0, "H", 17)
        return

class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        return

class Info(object):
    def __init__(self, is_ST, max_v, min_v):
        self.is_ST = is_ST
        self.max_v = max_v
        self.min_v = min_v

class Solution(object):
    def __init__(self):
        return

    def process(self, head):
        Max_v = 1e6
        Min_v = -1e6
        if head is None:
            return Info(True, Min_v, Max_v)
        leftInfo = self.process(head.left)
        rightInfo = self.process(head.right)
        is_ST = False
        max_v = max(max(leftInfo.max_v, rightInfo.max_v), head.val)
        min_v = min(min(leftInfo.min_v, rightInfo.min_v), head.val)
        if leftInfo.is_ST and rightInfo.is_ST \
            and leftInfo.max_v < head.val < rightInfo.min_v:
            is_ST = True
        return Info(is_ST, max_v, min_v)

if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)

    PrintBinaryTree().printTree(head)
    print('================>>>')
    pd = Node(3)
    pd.left = Node(5)
    pd.right = Node(6)
    PrintBinaryTree().printTree(pd)
    print('================>>>')
    # res = Node().process(head)
    # print(res.isBT)
    print(Solution().process(head).is_ST)