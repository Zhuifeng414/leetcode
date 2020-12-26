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

class PrintCommonPart():
    def __init__(self):
        return

    def printCommonPart(self, head1, head2):
        print('Common Part: ')
        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                head1 = head1.next
            elif head1.val > head2.val:
                head2 = head2.next
            else:
                print(head1.val)
                head1 = head1.next
                head2 = head2.next

if __name__ == '__main__':
    node1 = ListNode(2)
    node1.next = ListNode(3)
    node1.next.next = ListNode(5)
    node1.next.next.next = ListNode(6)

    node2 = ListNode(1)
    node2.next = ListNode(2)
    node2.next.next = ListNode(5)
    node2.next.next.next = ListNode(7)
    node2.next.next.next.next = ListNode(8)

    node1.printLinkedList(node1)
    node2.printLinkedList(node2)

    PrintCommonPart().printCommonPart(node1, node2)