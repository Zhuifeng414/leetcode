class Node(object):
    def __init__(self, val=None, next=None, random=None):
        self.val = val
        self.next = next

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

    def simple_remove(self, head):
        if head is None:
            return head
        check = []
        cur = head
        pre = None
        while cur is not None:
            if cur.val not in check:
                check.append(cur.val)
                pre = cur
                cur = cur.next
            else:
                cur = cur.next
                pre.next = cur
        return head

    def complicate_remove(self, head):
        if head is None:
            return head
        cur = head
        while cur is not None:
            pre = cur
            aft = cur.next
            while aft is not None:
                if cur.val == aft.val:
                    pre.next = aft.next
                else:
                    pre = pre.next
                aft = aft.next
            cur = cur.next
        return head
                    
if __name__ == '__main__':
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(1)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(2)
    Node().printList(head1)
    print('=====================>>>')
    #res = Node().simple_remove(head1)
    res = Node().complicate_remove(head1)
    Node().printList(res)

