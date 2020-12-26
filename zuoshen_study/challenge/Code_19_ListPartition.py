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

    def process(self, head, pivot):
        sH, sT = None, None
        eH, eT = None, None
        bH, bT = None, None
        next = None
        while head is not None:
            next = head.next
            head.next = None
            if head.val < pivot:
                if sH is None:
                    sH = head
                    sT = head
                else:
                    sT.next = head
                    sT = sT.next
            elif head.val == pivot:
                if eH is None:
                    eH = head
                    eT = head
                else:
                    eT.next = head
                    eT = eT.next
            else:
                if bH is None:
                    bH = head
                    bT = head
                else:
                    bT.next = head
                    bT = bT.next
            head = next
        if sT is not None:
            sT.next = eH
            eT = sT if eT is None else eT
        if eT is not None:
            eT.next = bH
        return sH if sH is not None else (eH if eH is not None else bH)

if __name__ == '__main__':
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(2)
    head1.next.next.next.next = Node(1)

    print('=====================>>>')
    Node().printList(head1)
    print('=====================>>>>')
    re_head = Node().process(head1,2)
    print('=====================>>>>')
    Node().printList(re_head)



