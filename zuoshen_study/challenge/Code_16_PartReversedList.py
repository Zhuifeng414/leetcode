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

    def partReverseList(self, head, frm, to):
        if frm < 1:
            print('error, frm is too small')
            return

        if head is None:
            return None
        # come to frm
        pa = None
        cur = head
        cur_index = 1
        while cur is not None:
            if cur_index == frm:
                break
            pa = cur
            cur = cur.next
            cur_index += 1
        # reverse frm --> to
        pre = None
        sa = cur
        while cur_index != to and cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
            cur_index += 1

        if cur_index <= to:
            print('error, to is too big')
            return None

        next = cur.next
        cur.next = pre
        sb = cur

        if pa is not None:
            pa.next = sb
            sa.next = next
            return head
        else:
            sa.next = next
            return sb


if __name__ == '__main__':
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    print('=====================>>>')
    Node().printList(head1)
    re_head = Node().partReverseList(head1, 1, 6)
    Node().printList(re_head)
    print('=====================>>>>')

