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

    def process(self, head):
        if head is None:
            return head
        cur = head
        while cur is not None:
            next = cur.next
            p = Node(cur.val)
            cur.next = p
            p.next = next
            cur = next
        cur = head
        while cur is not None:
            next = cur.next.next
            cur.next.random = cur.random.next if cur.random is not None else None
            cur = next
        cur = head
        phead = head.next
        p = phead
        while cur is not None:
            cur.next = cur.next.next
            p.next = p.next.next if cur.next is not None else None
            cur = cur.next
            p = p.next
        return head, phead

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.random = head.next.next
    head.next.random = head.next.next.next
    print('=====================>>>')
    res1, res2 = Node().process(head)
    print('res1>>=====================>>>>')
    Node().printList(res1)
    print('res2>>=====================>>>>')
    Node().printList(res2)




