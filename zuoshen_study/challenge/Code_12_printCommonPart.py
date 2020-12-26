class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printCommonPart(self, head1, head2):
        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                head1 = head1.next
            elif head1.val > head2.val:
                head2 = head2.next
            else:
                print('%s-->'%head1.val)
                head1 = head1.next
                head2 = head2.next
        return

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
    Node().printCommonPart(head1, head2)
