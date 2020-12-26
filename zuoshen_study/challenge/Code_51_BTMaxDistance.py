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

class Info(object):
    def __init__(self, h, dmax):
        self.h = h
        self.dmax = dmax

class Node(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def process(self, head):
        if head is None:
            return Info(0, 0)
        leftInfo = self.process(head.left)
        rightInfo = self.process(head.right)
        p1 = leftInfo.h + rightInfo.h
        p2 = leftInfo.dmax
        p3 = rightInfo.dmax
        dmax = max(max(p2, p3), p1)
        h = max(leftInfo.h, rightInfo.h) + 1
        return Info(h, dmax)

if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.left.right.left = Node(7)
    head.right.left = Node(6)
    PrintBinaryTree().printTree(head)
    print('================>>>')
    res = Node().process(head)
    print(res.dmax)

