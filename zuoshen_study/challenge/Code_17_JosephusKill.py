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


    def getLive(self, i, m):
        if i == 1:
            return i
        return (self.getLive(i-1, m) + m - 1)%i + 1

    def process(self, head, m):
        if head is None or head.next == head or m < 1:
            return head
        cur = head.next
        tmp = 1
        while cur != head:
            tmp += 1
            cur = cur.next
        print(tmp)
        index = self.getLive(tmp, m)
        print(index)
        for i in range(index-1):
            head = head.next
        head.next = head
        print(head.val)
        return head

if __name__ == '__main__':
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = head1
    print('=====================>>>')
    #Node().printList(head1)
    Node().process(head1, 3)

    print('=====================>>>>')

