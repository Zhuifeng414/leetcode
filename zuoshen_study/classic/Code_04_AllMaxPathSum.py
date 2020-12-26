class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## 打印二叉树
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
    def __init__(self, maxPathSum=0, fromHeadMaxPahtSum=0):
        self.maxPathSum = maxPathSum
        self.fromHeadMaxPahtSum = fromHeadMaxPahtSum

class AllMaxPathSum(object):
    def __init__(self):
        return

    def process(self, head):
        if head is None:
            return None

        leftInfo = self.process(head.left)
        rightInfo = self.process(head.right)

        p1, p2, p3, p4, p5, p6 = -999, -999, -999, -999, -999, -999
        if leftInfo is not None:
            p1 = leftInfo.maxPathSum
        if rightInfo is not None:
            p2 = rightInfo.maxPathSum
        p3 = head.val
        if leftInfo is not None:
            p4 = head.val + leftInfo.fromHeadMaxPahtSum
        if rightInfo is not None:
            p5 = head.val + rightInfo.fromHeadMaxPahtSum
        if leftInfo is not None and rightInfo is not None:
            p6 = head.val + leftInfo.fromHeadMaxPahtSum + rightInfo.fromHeadMaxPahtSum

        maxPathSum = max(max(max(p1, p2), max(p3, p4)), max(p5, p6))
        fromHeadMaxPahtSum = max(max(p3, p4), p5)

        return Info(maxPathSum, fromHeadMaxPahtSum)

if __name__ == '__main__':
    head = Node(5)
    head.left = Node(2)
    head.right = Node(7)
    head.left.left = Node(1)
    head.left.right = Node(3)
    head.right.right = Node(9)
    PrintBinaryTree().printTree(head)
    print('==================================')
    res = AllMaxPathSum().process(head)
    print(max(res.fromHeadMaxPahtSum, res.maxPathSum))