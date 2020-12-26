# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None or head.next.next is None:
            return None
        p = head.next
        q = head.next.next
        while p and q and p.next and q.next and q.next.next and p != q:
            print('pq pair', p.val, q.val)
            p = p.next
            q = q.next.next

        if p is None or q is None or p.next is None or q.next is None or q.next.next is None:
            return None
        else:
            print('first meet:', q.val)
            p = head
            index = 0

            while p.val != q.val:
                p = p.next
                q = q.next
                index += 1
        return p


if __name__ == '__main__':
    # (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    l1 = ListNode(3)
    l1.next = ListNode(2)
    l1.next.next = ListNode(0)
    l1.next.next.next = ListNode(-4)
    l1.next.next.next.next = l1.next
    #l1.printLinkedList(l1)

    res = Solution().detectCycle(l1)
    print(res.val)


