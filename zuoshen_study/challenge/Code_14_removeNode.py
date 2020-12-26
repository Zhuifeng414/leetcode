class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def removeMidNode(self, head):
        if head is None or head.next is None:
            return head
        if head.next.next is None:
            return head.next
        pre = head
        cur = head.next.next
        while cur.next is not None and cur.next.next is not None:
            pre = pre.next
            cur = cur.next.next
        pre.next = pre.next.next
        return head

    def removeByRatio(self, head, a, b):
        if a < 1 or a > b:
            return head
        n = 0
        cur = head
        while cur is not None:
            n += 1
            cur = cur.next
        n = int(a * n / b) + 1
        if n == 1:
            head = head.next
        if n > 1:
            cur = head
            n -= 1
            while n != 1:
                cur = cur.next
            cur.next = cur.next.next
        return head

if __name__ == '__main__':
    head1 = Node(1)
    head1.next = Node(3)
    head1.next.next = Node(5)
    head1.next.next.next = Node(7)
    print('=====================>>>')
    head2 = Node(1)
    head2.next = Node(2)
    head2.next.next = Node(3)
    print('=====================>>>>')

