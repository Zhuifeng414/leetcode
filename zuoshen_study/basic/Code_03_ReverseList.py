# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverseList(self, head):
        pre = None
        next = None
        #修改了原连标
        while head is not None:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre

    def printLinkedList(self, head):
        print('Linked List: ')
        while head is not None:
            print(head.val)
            head = head.next
        return

# Definition for double-linked list.
class DoubleListNode(object):
    def __init__(self, val=0, last=None, next=None):
        self.val = val
        self.next = next
        self.last = last

    def reverseList(self, head):
        pre = None
        next = None
        #修改了原连标
        while head is not None:
            next = head.next
            head.next = pre
            head.last = next
            pre = head
            head = next
        return pre

    def printLinkedList(self, head):
        print('Double Linked List: ')
        while head is not None:
            print(head.val)
            end = head
            head = head.next
        print('---')
        while end is not None:
            print(end.val)
            end = end.last
        return


if __name__ == '__main__':
    # list_node_test = ListNode()
    # head1 = ListNode(1)
    # head1.next = ListNode(2)
    # head1.next.next = ListNode(3)
    # list_node_test.printLinkedList(head1)
    # head1 = list_node_test.reverseList(head1)
    # list_node_test.printLinkedList(head1)

    list_node_test = DoubleListNode()
    head2 = DoubleListNode(1)
    head2.next = DoubleListNode(2)
    head2.next.last = head2
    head2.next.next = DoubleListNode(3)
    head2.next.next.last = head2.next
    head2.next.next.next = DoubleListNode(4)
    head2.next.next.next.last = head2.next.next
    print('before:')
    list_node_test.printLinkedList(head2)
    head2 = list_node_test.reverseList(head2)
    print('after:')
    list_node_test.printLinkedList(head2)
