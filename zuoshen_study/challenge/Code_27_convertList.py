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
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
        return

class Node(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printList(self, head):
        res = ''
        while head is not None:
            res += '%s-->' % head.val
            head = head.next
        print(res)
        return

    def reverseList(self, head):
        if head is None:
            return head
        pre = None
        cur = head
        n = 0
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
            n += 1
        return pre, n

    def inOrderToQueue(self, head, queue):
        if head is None:
            return None
        self.inOrderToQueue(head.left, queue)
        queue.append(head)
        self.inOrderToQueue(head.right, queue)

    def convertList(self, head):
        queue = []
        self.inOrderToQueue(head, queue)
        if len(queue) == 0:
            return None
        head = queue.pop(0)
        pre = head
        pre.left = None
        cur = None
        while len(queue) > 0:
            cur = queue.pop(0)
            pre.right = cur
            cur.left = pre
            pre = cur
        pre.right = None
        return head

    def process(self, head):
        if head is None:
            return Info(None, None)
        leftInfo = self.process(head.left)
        rightInfo = self.process(head.right)
        if leftInfo.end is not None:
            leftInfo.end.right = head
        head.left = leftInfo.end
        head.right = rightInfo.start
        if rightInfo.start is not None:
            rightInfo.start.left = head
        start = leftInfo.start if leftInfo.start is not None else head
        end = rightInfo.end if rightInfo.end is not None else head
        return Info(start, end)



if __name__ == '__main__':
    head1 = Node(6)
    head1.left = Node(4)
    head1.right = Node(7)
    head1.left.left = Node(2)
    head1.left.right = Node(5)
    head1.right.right = Node(9)
    head1.left.left.left = Node(1)
    head1.left.left.right = Node(3)
    head1.right.right.left = Node(8)
    print('=====================>>>')
    PrintBinaryTree().printTree(head1)
    print('=====================>>>')
    #res = Node().convertList(head1)
    res = Node().process(head1).start
    print('right>>=====================>>>')
    while res.right is not None:
        print(res.val)
        res = res.right
    print(res.val)
    print('left>>=====================>>>')
    while res.left is not None:
        print(res.val)
        res = res.left
    print(res.val)




