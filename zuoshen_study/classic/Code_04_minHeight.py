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
    def __init__(self, height=0):
        self.height = height

class MinHeight(object):
    def __init__(self):
        return

    def minHeight(self, head):
        if head is None:
            return None

        if head.left is None and head.right is None:
            return Info(1)

        leftInfo = self.minHeight(head.left)
        rightInfo = self.minHeight(head.right)

        leftheight = leftInfo.height if leftInfo is not None else 999
        rightheight = rightInfo.height if rightInfo is not None else 999

        height = 1 + min(leftheight, rightheight)
        return Info(height)

    def getRes(self, head):
        if head is None:
            return 0
        if head.left is None:
            res = MinHeight().minHeight(head.right).height + 1
        elif head.right is None:
            res = MinHeight().minHeight(head.left).height + 1
        else:
            res = MinHeight().minHeight(head).height
        return res

    def process(self, head):
        if head.left is None and head.right is None:
            return 1
        leftRes = 999
        rightRes = 999
        if head.left is not None:
            leftRes = 1 + self.process(head.left)
        if head.right is not None:
            rightRes = 1 + self.process(head.right)
        return min(leftRes, rightRes)

    def getRes2(self, head):
        if head is None:
            return 0
        return self.process(head)


if __name__ == '__main__':
    head = Node(1)
    #head.left = Node(2)
    head.right = Node(3)
    #head.left.left = Node(4)
    #head.left.right = Node(5)
    #head.right.left = Node(6)
    head.right.right = Node(7)

    print('printing=================>')
    PrintBinaryTree().printTree(head)
    print('res1=================>')
    print(MinHeight().getRes(head))
    print('res2=================>')
    print(MinHeight().getRes2(head))