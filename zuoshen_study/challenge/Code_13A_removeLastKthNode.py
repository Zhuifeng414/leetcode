class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def removeLastKthNode(self, head, lastKth):
        if head is None or lastKth < 1:
            return head
        cur = head
        while cur is not None:
            lastKth -= 1
            cur = cur.next
        if lastKth == 0:
            head = head.next
        if lastKth < 0:
            cur = head
            lastKth += 1
            while lastKth != 0:
                cur = cur.next
                lastKth += 1
            cur.next = cur.next.next
        return head

class DoubleNode(object):
    def __init__(self, val, last, next):
        self.val = val
        self.last = last
        self.next = next

    def removeLastKthNode(self, head, lastKth):
        if head is None or lastKth < 1:
            return head
        cur = head
        while cur is not None:
            lastKth -= 1
            cur = cur.next
        if lastKth == 0:
            return head.next
        if lastKth < 0:
            cur = head
            lastKth += 1
            while lastKth != 0:
                cur = cur.next
            newNext = cur.next.next
            cur.next = newNext
            if newNext is not None:
                newNext.last = cur
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

