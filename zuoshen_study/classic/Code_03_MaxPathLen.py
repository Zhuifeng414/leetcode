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
    def __init__(self, pathLen=0, height=0):
        self.pathLen = pathLen
        self.height = height

class MaxPathLen(object):
    def __init__(self):
        return

    def process(self, head):
        if head is None:
            return None

        leftInfo = self.process(head.left)
        rightInfo = self.process(head.right)
        # 经过 head
        pathLen = (leftInfo.height if leftInfo is not None else 0) \
             + (rightInfo.height if rightInfo is not None else 0) + 1
        # 不经过head
        # 左树不为空时
        if leftInfo is not None:
            pathLen = max(pathLen, leftInfo.pathLen)
        # 右树不为空时
        if rightInfo is not None:
            pathLen = max(pathLen, rightInfo.pathLen)
        height = max((leftInfo.height if leftInfo is not None else 0), (rightInfo.height if rightInfo is not None else 0)) + 1
        return Info(pathLen, height)

if __name__ == '__main__':
    head = Node(5)
    head.left = Node(2)
    head.right = Node(7)
    head.left.left = Node(1)
    head.left.right = Node(3)
    head.right.right = Node(9)
    PrintBinaryTree().printTree(head)
    print('==================================')
    res = MaxPathLen().process(head)
    print(max(res.pathLen, res.height + 1))