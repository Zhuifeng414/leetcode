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
    def __init__(self, isAllBST=False, maxBSTSize=0, max_val=0, min_val=0):
        self.isAllBST = isAllBST
        self.maxBSTSize = maxBSTSize
        self.max_val = max_val
        self.min_val = min_val

class BiggestSubBSTInTree(object):
    def __init__(self):
        return

    def func(self, head):
        if head is None:
            return None

        leftInfo = self.func(head.left)
        rightInfo = self.func(head.right)

        isAllBST = False
        maxBSTSize = 0
        p1 = 0
        p2 = 0
        p3 = 0
        if leftInfo is not None:
            p1 = leftInfo.maxBSTSize
        if rightInfo is not None:
            p2 = rightInfo.maxBSTSize
        # 1. 左子树整体是BST
        # 2. 右子树整体是BST
        # 3. 左子树 max_val < head.val
        # 4. 右子树 min_val > head.val
        if (leftInfo is None or leftInfo.isAllBST ) \
            and (rightInfo is None or rightInfo.isAllBST) \
            and (leftInfo is None or leftInfo.max_val < head.val) \
            and (rightInfo is None or rightInfo.min_val > head.val):
            p3 = (leftInfo.maxBSTSize if leftInfo is not None else 0) \
                + (rightInfo.maxBSTSize if rightInfo is not None else 0) + 1
            isAllBST = True

        maxBSTSize = max(p3, max(p1, p2))

        max_val = head.val
        min_val = head.val
        if leftInfo is not None:
            max_val = max(leftInfo.max_val, max_val)
            min_val = min(leftInfo.min_val, min_val)
        if rightInfo is not None:
            max_val = max(rightInfo.max_val, max_val)
            min_val = min(rightInfo.min_val, min_val)


        return Info(isAllBST, maxBSTSize, max_val, min_val)

if __name__ == '__main__':
    head = Node(5)
    head.left = Node(2)
    head.right = Node(7)
    head.left.left = Node(1)
    head.left.right = Node(3)
    head.right.right = Node(9)
    PrintBinaryTree().printTree(head)
    print('==================================')
    print(BiggestSubBSTInTree().func(head).maxBSTSize)
