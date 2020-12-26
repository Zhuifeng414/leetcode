class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self, head):
        res = ''
        while head is not None:
            res += '%s-->'%head.val
            head = head.next
        print(res)
        return

    def process(self, head):
        if head is None or head.next is None:
            return True
        fast = head.next
        slow = head
        slow_next = slow.next
        mode = 1
        pre = None
        while fast is not None and fast.next is not None:
            next = slow.next
            slow.next = pre
            pre = slow
            slow = next
            slow_next = slow.next
            # 4
            if fast.next.next is not None:
                fast = fast.next.next
                mode = 1
            # 5
            else:
                fast = fast.next
                mode = 2
        slow.next = pre
        if mode == 1:
            p1 = slow
            p2 = slow_next
        if mode == 2:
            p1 = pre
            p2 = slow_next
        print('p1>>=====================>>>')
        Node().printList(p1)
        print('p2>>=====================>>>')
        Node().printList(p2)

        while p1 is not None and p2 is not None:
            if p1.val == p2.val:
                p1 = p1.next
                p2 = p2.next
            else:
                return False
        return True

if __name__ == '__main__':
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(2)
    head1.next.next.next.next = Node(1)

    print('=====================>>>')
    Node().printList(head1)
    print('=====================>>>>')
    print(Node().process(head1))


