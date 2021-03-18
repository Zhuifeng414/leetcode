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

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == right:
            return head
        aft_pr = head
        index = 1
        pre_pl = None
        aft_pr = None
        while index <= right:
            if index == left - 1:
                pre_pl = aft_pr
            aft_pr = aft_pr.next
            index += 1

        if not pre_pl:
            t = pre_pl.next
            pre = pre_pl.next
        else:
            t =
        cur = pre.next
        for i in range(right-left):
            aft = cur.next
            cur.next = pre
            pre = cur
            cur = aft

        if not pre_pl:
            pre_pl.next = pre
        if not aft_pr:
            t.next = aft_pr
        return head

        #ListNode().printLinkedList(head)

    def my_code(self, head, left, right):
        dummy_node = ListNode(-1)
        dummy_node = head
        pre = dummy_node
        for i in range(left-1):
            pre = pre.next

        cur = pre.next
        for i in range(right-left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy_node.next

# class Solution:
#     def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
#         # 设置 dummyNode 是这一类问题的一般做法
#         dummy_node = ListNode(-1)
#         dummy_node.next = head
#         pre = dummy_node
#         for _ in range(left - 1):
#             pre = pre.next
#
#         cur = pre.next
#         for _ in range(right - left):
#             next = cur.next
#             cur.next = next.next
#             next.next = pre.next
#             pre.next = next
#         return dummy_node.next


if __name__ == '__main__':
    head1 = ListNode(3)
    head1.next = ListNode(5)
    # head1.next.next = ListNode(3)
    # head1.next.next.next = ListNode(4)
    # head1.next.next.next.next = ListNode(5)
    Solution().reverseBetween(head1, 1, 2)
