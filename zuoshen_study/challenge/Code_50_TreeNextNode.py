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

class Node(object):
    def __init__(self, val=None, left=None, right=None, parent = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def getLeftMost(self, node):
        if node is None:
            return node
        while node.left is not None:
            node = node.left
        return node

    def getNextNode(self, head, node):
        if node is None:
            return node

        if node.right is not None:
            return self.getLeftMost(node.right)
        else:
            parent = node.parent
            while parent is not None and parent.left != node:
                node = parent
                parent = node.parent
        return parent

if __name__ == '__main__':
    head = Node(1)
    head.parent = None
    head.left = Node(2)
    head.left.parent = head
    head.right = Node(3)
    head.right.parent = head
    head.left.left = Node(4)
    head.left.left.parent = head.left
    head.left.right = Node(5)
    head.left.right.parent = head.left
    PrintBinaryTree().printTree(head)
    print('================>>>')
    res = Node().getNextNode(head, head.left.left)
    print(res.val)
