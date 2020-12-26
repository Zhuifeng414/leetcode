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

    def process(self, head):
        Min_Val = -1e6
        Max_Val = 1e6
        if head is None:
            return Info(None, 0, Max_Val, Min_Val)
        leftInfo = self.process(head.left)
        rightInfo = self.process(head.right)

        min_val = min(head.val, min(leftInfo.min_val, rightInfo.min_val))
        max_val = max(head.val, max(leftInfo.max_val, rightInfo.max_val))

        maxBSTSize = max(leftInfo.maxBSTSize, rightInfo.maxBSTSize)

        maxBSTHead = leftInfo.maxBSTHead if leftInfo.maxBSTSize >= rightInfo.maxBSTSize else rightInfo.maxBSTHead

        if leftInfo.maxBSTHead == head.left and rightInfo.maxBSTHead == head.right \
                and leftInfo.max_val < head.val < rightInfo.min_val:
            maxBSTSize = leftInfo.maxBSTSize + rightInfo.maxBSTSize + 1
            maxBSTHead = head

        return Info(maxBSTHead, maxBSTSize, min_val, max_val)


if __name__ == '__main__':
    head = Node(10)
    head.left = Node(4)
    head.right = Node(14)
    head.left.left = Node(2)
    head.left.right = Node(5)
    head.right.left = Node(11)
    head.right.right = Node(15)
    print('================>>>')
    res = Node().process(head)
    print(res.maxBSTSize)
