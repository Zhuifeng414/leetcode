class Node(object):
    def __init__(self, val=None, next=None, random=None):
        self.val = val
        self.next = next

    def printList(self, head):
        res = ''
        while head is not None:
            res += '%s-->'%head.val
            head = head.next
        print(res)
        return

    def reverseList(self, head):
        if head is None:
            return head
        pre = None
        cur = head
        n = 0
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
            n += 1
        return pre, n

    def getLoopNode(self, head):
        if head is None:
            return None
        slow, fast = head, head
        mode = 0
        while fast is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                mode = 1
                break
        if mode == 1:
            fast = head
            while fast != slow:
                fast =fast.next
                slow = slow.next
            return fast
        else:
            return None

    def noLoope(self, head1, head2, mode=None):
        if head1 is None or head2 is None:
            return False, Node(-1)
        cur1 = head1
        n1 = 1
        cur2 = head2
        n2 = 1
        while cur1.next is not mode:
            n1 += 1
            cur1 = cur1.next
        while cur2.next is not mode:
            cur2 = cur2.next
            n2 += 1
        if cur1 != cur2:
            if mode is None:
                return False, Node(-1)
            else:
                return True, mode
        else:
            if n1 < n2:
                head1, head2 = head2, head1
                n1, n2 = n2, n1
            for i in range(n1-n2):
                head1 = head1.next
            while head1 is not mode and head1 != head2:
                head1 = head1.next
                head2 = head2.next
            if head1 is mode:
                return False, Node(-1)
            return True, head1

    def bothLoop(self, head1, p1, head2, p2):
        if p1 == p2:
            res = self.noLoope(head1, head2, p1)
            return res
        if p1 != p2:
            cur = p1.next
            while cur != p1:
                if cur == p2:
                    return True, p1
                cur = cur.next
            return False, Node(-1)

    def main_method(self, head1, head2):
        p1 = Node().getLoopNode(head1)
        p2 = Node().getLoopNode(head2)
        if p1 is None and p2 is not None \
            or p1 is not None and p2 is None:
            return False
        if p1 is None and p2 is None:
            return self.noLoope(head1, head2)
        if p1 is not None and p2 is not None:
            return self.bothLoop(head1, p1, head2, p2)

if __name__ == '__main__':
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = head1.next.next
    #Node().printList(head1)
    print('=====================>>>')
    # head2 = Node(11)
    # head2.next = Node(12)
    # head2.next.next = Node(13)
    # head2.next.next.next = Node(14)
    # head2.next.next.next.next = Node(15)
    # head2.next.next.next.next.next = head2.next.next
    #Node().printList(head2)

    head2 = Node(11)
    head2.next = Node(12)
    head2.next.next = head1.next.next
    # print('=====================>>>')
    # p1 = Node().getLoopNode(head1)
    # print(p1.val)
    # print('=====================>>>')
    # p2 = Node().getLoopNode(head2)
    # print(p2.val)
    # print('=====================>>>')
    # res = Node().bothLoop(head1, p1, head2, p2)
    # print(res[0], res[1].val)
    print('=====================>>>')
    res = Node().main_method(head1, head2)
    print(res[0], res[1].val)
