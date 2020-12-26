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
    def __init__(self, pathSum):
        self.pathSum = pathSum

class MaxPathSumInBT(object):
    def __init__(self):
        return

    def func(self, head):
        if head is None:
            return None
        leftInfo = self.func(head.left)
        rightInfo = self.func(head.right)

        if leftInfo is not None:
            p1 = head.val + leftInfo.pathSum
        if rightInfo is not None:
            p2 = head.val + rightInfo.pathSum
        # 两边都为空，返回节点值，此时已到叶节点
        if leftInfo is None and rightInfo is None:
            return Info(head.val)
        # 两边都不为空，返回最大路径
        elif head.left is not None and head.right is not None:
            return Info(max(p1, p2))
        # 一个为空一个不为空
        else:
            if head.left is None:
                return Info(p2)
            else:
                return Info(p1)

if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(7)
    head.right.right = Node(5)
    PrintBinaryTree().printTree(head)
    print('==================================')
    print(MaxPathSumInBT().func(head).pathSum)

