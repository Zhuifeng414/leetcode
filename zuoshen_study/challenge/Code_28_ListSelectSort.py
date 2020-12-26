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

    def getSmallestPreNode(self, head):
        smallPre = None
        small = head
        pre = head
        cur = head.next
        while cur is not None:
            if cur.val < small.val:
                smallPre = pre
                small = cur
            pre = cur
            cur = cur.next
        return smallPre

    def selectionSort(self, head):
        tail = None
        cur = head
        smallPre = None
        small = None
        while cur is not None:
            small = cur
            smallPre = self.getSmallestPreNode(cur)
            if smallPre is not None:
                small = smallPre.next
                smallPre.next = small.next
            cur = (cur.next if cur == small else cur)
            if tail is None:
                Newhead = small
            else:
                tail.next = small
            tail = small
        return Newhead

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





