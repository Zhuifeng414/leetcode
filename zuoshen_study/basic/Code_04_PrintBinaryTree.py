class Node(object):
    def __init__(self, val=0, left=None ,right=None):
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

if __name__ == '__main__':
    head = Node(1)
    PrintBinaryTree().printTree(head)
    head.left = Node(-2)
    head.right = Node(3)
    head.left.left = Node(0)
    head.right.left = Node(5)
    head.right.right = Node(67)
    head.left.left.right = Node(77)
    PrintBinaryTree().printTree(head)
