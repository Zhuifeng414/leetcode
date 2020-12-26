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

# 输入 str 和 match
# 如果str含有子串match,返回match在str中开始的位置，否则返回-1
# s = 'acbc'
# m = 'bc'
# 输出 2
class KMP(object):
    def __init__(self):
        return

    def getNextArray(self, ms):
        if len(ms) == 1:
            return [-1]
        next = [0 for i in range(len(ms))]
        next[0] = -1
        next[1] = 0
        pos = 2
        cn = 0
        while pos < len(next):
            if ms[pos - 1] == ms[cn]:
                cn += 1
                next[pos] = cn
                pos += 1
            elif cn > 0:
                cn = next[cn]
            else:
                next[pos] = 0
                pos += 1
        return next

    def getIndexOf(self, s, m):
        if len(s) == 0 or len(m) < 1 or len(s) < len(m):
            return -1
        si = 0
        mi = 0
        next = self.getNextArray(m)
        while si < len(s) and mi < len(m):
            if s[si] == m[mi]:
                si += 1
                mi += 1
            elif next[mi] == -1:
                si += 1
            else:
                mi = next[mi]
        return (si - mi) if mi == len(m) else -1

class Info(object):
    def __init__(self, isBT, h):
        self.isBT = isBT
        self.h = h

class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        return

    def process(self, head):
        if head is None:
            return Info(True, 0)

        leftInfo = self.process(head.left)
        rightInfo = self.process(head.right)

        isBT = False
        h = max(leftInfo.h, rightInfo.h) + 1
        if leftInfo.isBT and rightInfo.isBT and abs(leftInfo.h - rightInfo.h) <=1:
            isBT = True
        return Info(isBT, h)

if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    #head.left.right = Node(5)
    head.right.left = Node(5)
    head.right.right = Node(6)
    head.right.left.left = Node(7)
    head.right.left.left.right = Node(8)
    PrintBinaryTree().printTree(head)
    print('================>>>')
    pd = Node(3)
    pd.left = Node(5)
    pd.right = Node(6)
    PrintBinaryTree().printTree(pd)
    print('================>>>')
    res = Node().process(head)
    print(res.isBT)
