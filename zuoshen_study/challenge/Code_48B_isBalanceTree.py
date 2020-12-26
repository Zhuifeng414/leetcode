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
    def __init__(self, is_BT, mode, h):
        self.is_BT = is_BT
        self.mode = mode
        self.h = h

class Solution(object):
    def __init__(self):
        return

    def process(self, head):
        if head is None:
            return Info(True, False, 0)
        leftInfo = self.process(head.left)
        rightInfo = self.process(head.right)
        is_BT = False
        h = max(leftInfo.h, rightInfo.h) + 1

        mode = False
        if leftInfo.mode or rightInfo.mode \
            or leftInfo.h != rightInfo.h:
            mode = True

        if leftInfo.is_BT and rightInfo.is_BT \
        and leftInfo.h - rightInfo.h >= 0\
        and leftInfo.h - rightInfo.h <= 1\
        and (leftInfo.mode and not rightInfo.mode
        or not leftInfo.mode and not rightInfo.mode):
            is_BT = True
        return Info(is_BT, mode, h)

if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    PrintBinaryTree().printTree(head)
    print('================>>>')
    pd = Node(3)
    pd.left = Node(5)
    pd.right = Node(6)
    PrintBinaryTree().printTree(pd)
    print('================>>>')
    # res = Node().process(head)
    # print(res.isBT)
    print(Solution().process(head).is_BT)