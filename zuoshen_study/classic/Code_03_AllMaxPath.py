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
    def __init__(self, val, leftSum, rightSum):
        self.val = val
        self.leftSum = leftSum
        self.rightSum = rightSum

class MaxPathSum(object):
    def __init__(self):
        return

    def func(self, head):
        if head is None:
            return None

        leftInfo = self.func(head.left)
        rightInfo = self.func(head.right)


        p1 = leftInfo.leftSum if leftInfo is not None else 0
        p2 = rightInfo.rightSum if rightInfo is not None else 0

        if head.val > 0:
            return Info(head.val, head.val+p1, head.val+p2)
        else:
            return Info(0, p1, p2)

class Info2(object):
    def __init__(self, fromHeadMaxPathSum, allMaxPathSum):
        self.fromHeadMaxPathSum = fromHeadMaxPathSum
        self.allMaxPathSum = allMaxPathSum

class MaxPathSum2(object):
    def __init__(self):
        return

    def func2(self, head):
        if head is None:
            return None

        leftInfo = self.func2(head.left)
        rightInfo = self.func2(head.right)
        p1 = head.val
        p2 = head.val + (leftInfo.fromHeadMaxPathSum if leftInfo is not None else 0)
        p3 = head.val + (rightInfo.fromHeadMaxPathSum if rightInfo is not None else 0)
        fromHeadMaxPathSum = max(p1, max(p2, p3))
        allMaxPathSum = fromHeadMaxPathSum
        if leftInfo is not None:
            allMaxPathSum = max(allMaxPathSum, leftInfo.allMaxPathSum)
        if rightInfo is not None:
            allMaxPathSum = max(allMaxPathSum, rightInfo.allMaxPathSum)
        return Info2(fromHeadMaxPathSum, allMaxPathSum)

if __name__ == '__main__':
    head = Node(5)
    head.left = Node(-2)
    head.right = Node(-1)
    head.left.left = Node(1)
    head.left.right = Node(3)
    head.right.right = Node(-9)
    PrintBinaryTree().printTree(head)
    print('2==================================')
    res = MaxPathSum2().func2(head)
    #print(max(res.val, max(res.leftSum, res.rightSum)))
    print(res.allMaxPathSum)
    print('1==================================')
    res = MaxPathSum().func(head)
    print(max(res.val, max(res.leftSum, res.rightSum)))
    #print(res.allMaxPathSum)