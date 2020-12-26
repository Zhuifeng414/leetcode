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
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def mostLeftLevel(self, node, level):
        while node is not None:
            level += 1
            node = node.left
        return level - 1

    def process(self, node, l, h):
        if l == h:
            return 1
        if self.mostLeftLevel(node.right, l+1) == h:
            return (1 << (h-l)) + self.process(node.left, l+1, h)
        else:
            return (1 << (h-l-1)) + self.process(node.right, l+1, h)

if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.left.right.left = Node(7)
    head.right.left = Node(6)
    PrintBinaryTree().printTree(head)
    print('================>>>')


