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

class IsPalindromeList:
    def __init__(self):
        return

    def listPartition1(self, head, pivot):
        if head is None:
            return head

        cur = head
        nodeArr = []
        while cur is not None:
            nodeArr.append(cur)
            cur = cur.next

        self.arrPartition(nodeArr, pivot)
        for i in range(1, len(nodeArr)):
            nodeArr[i - 1].next = nodeArr[i]
        nodeArr[i].next = None
        return nodeArr[0]


    def arrPartition(self, nodeArr, pivot):
        small = -1
        big = len(nodeArr)
        index = 0
        while index < big:
            if nodeArr[index].val < pivot:
                small += 1
                self.swap(nodeArr, small, index)
                index += 1
            elif nodeArr[index].val > pivot:
                big -= 1
                self.swap(nodeArr, big, index)
            else:
                index += 1
        return

    def swap(self, nodeArr, a, b):
        tmp = nodeArr[a]
        nodeArr[a] = nodeArr[b]
        nodeArr[b] = tmp

    def listPartition2(self, head, pivot):
        sH, sT = None, None
        eH, eT = None, None
        bH, bT = None, None
        while head is not None:
            next = head.next
            head.next = None
            if head.val < pivot:
                if sH is None:
                    sH = head
                    sT = head
                else:
                    sT.next = head
                    sT = head
            elif head.val == pivot:
                if eH is None:
                    eH = head
                    eT = head
                else:
                    eT.next = head
                    eT = head
            else:
                if bH is None:
                    bH = head
                    bT = head
                else:
                    bT.next = head
                    bT = head
            head = next

        if sT is not None:
            sT.next = eH
            eT = eT if eT is not None else sT
        if eT is not None:
            eT.next = bH

        if sH is not None:
            return sH
        elif eH is not None:
            return eH
        else:
            return bH

if __name__ == '__main__':
    print('isPalindrome:')
    node1 = ListNode(2)
    node1.next = ListNode(3)
    node1.next.next = ListNode(3)
    node1.next.next.next = ListNode(1)
    node1.next.next.next.next = ListNode(4)
    node1.next.next.next.next.next = ListNode(1)
    node1.next.next.next.next.next.next = ListNode(5)
    print('init list: ')
    node1.printLinkedList(node1)
    #node2 = IsPalindromeList().listPartition1(node1, 3)
    node2 = IsPalindromeList().listPartition2(node1, 3)
    print('ans is: ')
    while node2 is not None:
        print(node2.val)
        node2 = node2.next
    print('ans is: ')
    #node2.printLinkedList(node2)
