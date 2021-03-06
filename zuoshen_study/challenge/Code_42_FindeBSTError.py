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
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def process(self, head):
        errs = [Node(), Node()]
        if head is None:
            return errs
        pre = None
        stack = []
        while len(stack) > 0 or head is not None:
            if head is not None:
                stack.append(head)
                head = head.left
            else:
                head = stack.pop()
                if pre is not None and pre.val > head.val:
                    errs[0] = errs[0] if errs[0] is not None else pre
                    errs[1] = head
                pre = head
                head = head.right
        return errs



if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    #head.left.right = Node(5)
    head.right.left = Node(5)
    head.right.right = Node(6)
    head.right.left.left = Node(7)
    head.right.left.right = Node(8)
    print('================>>>')
    #Node().printByLevel(head)
