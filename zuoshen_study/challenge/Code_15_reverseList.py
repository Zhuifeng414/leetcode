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

    def reverseList(self, head):
        pre = None
        next = None
        while head is not None:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre

class DoubelNode(object):
    def __init__(self, val=None, last=None, next=None):
        self.val = val
        self.last = last
        self.next = next
        return

    def printList(self, head):
        next_res = ''
        while head.next is not None:
            next_res += '%s---->'%head.val
            head = head.next
        next_res += '%s---->' % head.val
        print('next: %s'%next_res)

        last_res = ''
        while head.last is not None:
            last_res += '%s<---'%head.val
            head = head.last
        last_res += '%s<---' % head.val
        print('last: %s'%last_res)
        return

    def reverseList(self, head):
        pre = None
        next = None
        while head is not None:
            next = head.next
            head.next = pre
            head.last = next
            pre = head
            head = next
        return pre

if __name__ == '__main__':
    head1 = Node(1)
    head1.next = Node(3)
    head1.next.next = Node(5)
    head1.next.next.next = Node(7)
    print('=====================>>>')
    head2 = DoubelNode(1)
    head2.last =  None
    head2.next = DoubelNode(2)
    head2.next.last = head2
    head2.next.next = DoubelNode(3)
    head2.next.next.last = head2.next
    print('=====================>>>>')
    # Node().printList(head1)
    # re_head = Node().reverseList(head1)
    # Node().printList(re_head)
    print('=====================>>>>')
    DoubelNode().printList(head2)
    print('=====================>>>>')
    re_head = DoubelNode().reverseList(head2)
    DoubelNode().printList(re_head)

