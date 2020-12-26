class Node(object):
    def __init__(self, val=None, next=None, random=None):
        self.val = val
        self.next = next

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

    def deleteValue(self, head, value):
        if head is None:
            return head
        pre = None
        cur = head
        tmp = 0
        while cur is not None:
            if cur.val != value:
                if tmp == 0:
                    tmp = 1
                    newHead = cur
                pre = cur
                cur = cur.next
            else:
                if pre is not None:
                    pre.next = cur.next
                cur = cur.next
        return newHead

if __name__ == '__main__':
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(1)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(2)
    Node().printList(head1)
    print('=====================>>>')
    res = Node().deleteValue(head1, 2)
    Node().printList(res)


