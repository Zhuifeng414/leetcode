# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return -1
        pf, ps = head, head
        while pf and pf.next and pf != ps:
            pf = pf.next.next
            ps = ps.next
        if pf == ps:
            pf = head
            while pf != ps:
                pf = pf.next
                ps = ps.next
            return pf
        else:
            return -1
        return -1