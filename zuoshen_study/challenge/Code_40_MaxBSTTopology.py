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
    def __init__(self, psum, h):
        self.psum = psum
        self.h = h


class Info(object):
    def __init__(self, maxBSTHead, maxBSTSize, min_val, max_val):
        self.maxBSTHead = maxBSTHead
        self.maxBSTSize = maxBSTSize
        self.min_val = min_val
        self.max_val = max_val


class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isBSTNode(self, h, n, value):
        if h is None:
            return False
        if h == n:
            return True
        return self.isBSTNode(h.left if value < h.val else h.right, n, value)

    def maxTopo(self, h, n):
        if h is not None and n is not None and self.isBSTNode(h, n, n.val):
            return self.maxTopo(h, n.left) + self.maxTopo(h, n.right) + 1
        return 0

    def bstTopoSize(self, head):
        if head is None:
            return 0
        p1 = self.maxTopo(head, head)
        p2 = self.bstTopoSize(head.left)
        p3 = self.bstTopoSize(head.right)
        res = max(max(p2, p3), p1)
        return res




if __name__ == '__main__':
    head = Node(10)
    head.left = Node(4)
    head.right = Node(14)
    head.left.left = Node(2)
    head.left.right = Node(5)
    head.right.left = Node(11)
    head.right.right = Node(15)
    print('================>>>')

