class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class PrintBinaryTree():
    def __init__(self):
        return

    def getSpace(self, num):
        space = " " * num
        return space

    def printInOrder(self, head, height, to, leng):
        if head is None:
            return
        self.printInOrder(head.right, height+1, 'v', leng)
        val = str(to) + str(head.val) + str(to)
        #print('val', val)
        lenM = len(str(val))
        lenL = int((leng - lenM) / 2)
        lenR = leng - lenM - lenL
        val = self.getSpace(lenL) + val + self.getSpace(lenR)
        print(self.getSpace(height * leng) + val)
        self.printInOrder(head.left, height+1, '^', leng)

    def printTree(self, head):
        print('Binary Tree')
        self.printInOrder(head, 0, "H", 17)
        return

class CompleteTreeNodeNumber:
    def __init__(self):
        return

    def mostLeftLevel(self, node, level):
        while node is not None:
            level += 1
            node = node.left
        return level - 1

    def bs(self, node, l, h):
        if l == h:
            return 1
        if self.mostLeftLevel(node.right, l + 1) == h:
            return (1 << (h - l)) + self.bs(node.right, l+1, h)
        else:
            return (1 << (h - l -1)) + self.bs(node.left, l+1, h)

    def nodeNum(self, head):
        if head is None:
            return 0
        return self.bs(head, 1, self.mostLeftLevel(head, 1))


if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.right.left = Node(6)
    head.right.right = Node(7)
    head.left.left.left = Node(8)
    head.left.left.right = Node(9)
    head.left.right.left = Node(10)
    PrintBinaryTree().printTree(head)

    print(CompleteTreeNodeNumber().nodeNum(head))