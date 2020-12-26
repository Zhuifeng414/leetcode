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
    def __init__(self, pathSum=0):
        self.pathSum = pathSum

class MaxPathSum(object):
    def __init__(self):
        return

    def func(self, head):
        if head is None:
            return None

        leftInfo = self.func(head.left)
        rightInfo = self.func(head.right)


        p1 = leftInfo.pathSum if leftInfo is not None else 0
        p2 = rightInfo.pathSum if rightInfo is not None else 0

        if head.val > 0:
            return Info(head.val + max(p1, p2))
        else:
            return Info(max(p1, p2))

if __name__ == '__main__':
    head = Node(5)
    head.left = Node(2)
    head.right = Node(7)
    head.left.left = Node(1)
    head.left.right = Node(3)
    head.right.right = Node(9)
    PrintBinaryTree().printTree(head)
    print('==================================')
    print(MaxPathSum().func(head).pathSum)