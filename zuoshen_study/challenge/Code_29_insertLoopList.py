class Node(object):
    def __init__(self, val=None, next=None):
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

    def insertLoopList(self, head, val):
        ph = Node(val)
        if head is None:
            ph.next = ph
            return ph
        if val <= head.val:
            ph.next = head
            return ph
        pre = head
        cur = head.next
        while cur != head:
            if pre.val <= val <= cur.val:
                pre.next = ph
                ph.next = cur
                return head
            if pre.val <= cur.val < val:
                pre = cur
                cur = cur.next
            if val > pre.val >= cur.val:
                pre.next = ph
                ph.next = cur
                return head

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = head
    print('=====================>>>')
    #Node().printList(head)
    res = Node().insertLoopList(head, 0)
    print('=====================>>>')





