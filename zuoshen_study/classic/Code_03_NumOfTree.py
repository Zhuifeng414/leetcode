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


class NumOfTree(object):
    def __init__(self):
        return

    def func(self, n):
        if n == 0:
            return 1
        if n <= 2:
            return n
        res = 0
        for i in range(1, n):
            res += self.func(i) * self.func(n - i)
        return res

    def dps(self, n):
        if n == 0:
            return 1
        if n <= 2:
            return n

        dp = [0 for i in range(n+1)]

        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            for j in range(1, i):
                dp[i] += dp[j] * dp[i - j]
        return dp[n]

if __name__ == '__main__':
    # head = Node(1)
    # head.left = Node(2)
    # head.right = Node(3)
    # head.left.left = Node(4)
    # head.left.right = Node(7)
    # head.right.right = Node(5)
    # PrintBinaryTree().printTree(head)
    # print('==================================')
    #print(MaxPathSumInBT().func(head).pathSum)
    print(NumOfTree().func(5))
    # print('==================================')
    print(NumOfTree().dps(5))

