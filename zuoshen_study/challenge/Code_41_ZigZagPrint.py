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

    def printByLevel(self, head):
        if head is None:
            return
        queue = []
        level = 1
        last = head
        nlast = None
        queue.append(head)
        #print('Level: %s'%level)
        #level += 1
        res = ''
        while len(queue) > 0:
            head = queue.pop(0)
            #print('%s '%head.val)
            res += '%s '%head.val
            if head.left is not None:
                queue.append(head.left)
                nlast = head.left
            if head.right is not None:
                queue.append(head.right)
                nlast = head.right

            if head == last and len(queue) > 0:
                print('Level: [%s]'%level, res)
                level += 1
                res = ''
                last = nlast
        print('Level: [%s]'%level, res)
        return



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
    Node().printByLevel(head)
