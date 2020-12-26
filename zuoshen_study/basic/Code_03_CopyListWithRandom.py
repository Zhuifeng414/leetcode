class ListNode(object):
    def __init__(self, val=0, next=None, rand=None):
        self.val = val
        self.next = next
        self.rand = rand

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

    def printRandLinkedList(self, head):
        cur = head
        val_list = []
        rand_list = []
        while cur is not None:
            val_list.append(cur.val)
            if cur.rand is not None:
                rand_list.append(cur.rand.val)
            else:
                rand_list.append('- ')
            cur = cur.next
        print('order: ', val_list)
        print('rand: ', rand_list)

class CopyListWithRandom:
    def __init__(self):
        return

    def copyListWithRand1(self, head):
        cur = head
        Hash = {None: None}
        while cur is not None:
            Hash[cur] = ListNode(cur.val)
            cur = cur.next

        cur = head
        while cur is not None:
            Hash[cur].next = Hash[cur.next]
            Hash[cur].rand = Hash[cur.rand]
            cur = cur.next

        return Hash[head]

    def copyListWithRand2(self, head):
        if head is None:
            return None

        cur = head
        next = None
        while(cur is not None):
            next = cur.next
            cur.next = ListNode(cur.val)
            cur.next.next = next
            cur = next

        cur = head
        # copy
        while cur:
            next = cur.next.next
            curCopy = cur.next
            curCopy.rand = cur.rand.next if cur.rand is not None else None
            cur = next

        res = head.next
        cur = head

        # split
        while cur:
            next = cur.next.next
            curCopy = cur.next
            cur.next = next
            curCopy.next = next.next if next is not None else None
            cur = next

        return res

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    head.rand = head.next.next.next.next.next; # 1 -> 6
    head.next.rand = head.next.next.next.next.next; # 2 -> 6
    head.next.next.rand = head.next.next.next.next; # 3 -> 5
    head.next.next.next.rand = head.next.next; # 4 -> 3
    head.next.next.next.next.rand = None; # 5 -> null
    head.next.next.next.next.next.rand = head.next.next.next; # 6 -> 4

    ListNode().printRandLinkedList(head)
    print('-----------------')
    res1 = CopyListWithRandom().copyListWithRand1(head)
    ListNode().printRandLinkedList(res1)

    print('-----------------')
    res2 = CopyListWithRandom().copyListWithRand2(head)
    ListNode().printRandLinkedList(res2)