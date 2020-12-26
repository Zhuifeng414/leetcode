class Node(object):
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

    def printList(self, head):
        res = ''
        while head is not None:
            res += '%s-->'%head.val
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

    def process(self, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        p1, n1 = self.reverseList(head1)
        p2, n2 = self.reverseList(head2)
        # p1 longer
        if n1 < n2:
            p1, p2 = p2, p1

        a, b = 0, 0
        res_head = p1
        pre = p1
        while p1 is not None:
            tmp = p1.val + (p2.val if p2 is not None else 0) + a
            a, b = tmp//10, tmp%10
            p1.val = b
            pre = p1
            p1 = p1.next
            p2 = p2.next if p2 is not None else None
        if a > 0:
            pre.next = Node(a)
        return self.reverseList(res_head)

if __name__ == '__main__':
    head1 = Node(9)
    head1.next = Node(3)
    head1.next.next = Node(7)
    Node().printList(head1)
    print('=====================>>>')
    head2 = Node(6)
    head2.next = Node(4)
    Node().printList(head2)
    print('=====================>>>')
    res, n = Node().process(head2, head1)
    Node().printList(res)





