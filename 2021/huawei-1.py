# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def printLinkedList(self, head):
        while head:
            print(str(head.val) + ' -> ', end='' )
            head = head.next
        print('')


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1.val == 0:
            return l2
        if l2.val == 0:
            return l1

        l1 = self.rever_list(l1)
        l2 = self.rever_list(l2)
        l1.printLinkedList(l1)
        l2.printLinkedList(l2)
        flag = 0
        res_head = ListNode(0)
        res = res_head
        while l1 or l2:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            remain = (val1 + val2 + flag) % 10
            flag = (val1 + val2 + flag) // 10
            #print(val1, val2, remain, flag)
            res.next = ListNode(remain)
            res = res.next
            res_head.printLinkedList(res_head)
            l1 = l1.next if l1 is not None else l1
            l2 = l2.next if l2 is not None else l2
        if flag == 1:
            res = ListNode(1)
            res = res.next
        return self.rever_list(res_head.next)

    def rever_list(self, l):
        pre = None
        aft = None
        while l is not None:
            aft = l.next
            l.next = pre
            pre = l
            l = aft
        return pre



if __name__ == '__main__':
    # (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    l1 = ListNode(7)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(3)
    #l1.printLinkedList(l1)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    #l2.printLinkedList(l2)

    res = Solution().addTwoNumbers(l1, l2)
    res.printLinkedList(res)


