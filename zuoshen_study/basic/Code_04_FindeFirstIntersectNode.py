class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class FindeFirstIntersectNode:
    def __init__(self):
        return

    # 这是什么魔术？
    def getLoopNode(self, head):
        if head == None or head.next == None or head.next.next == None:
            return None

        slow = head.next
        fast = head.next.next
        while slow != fast:
            if fast.next == None or fast.next.next == None:
                return None
            fast = fast.next.next
            slow = slow.next

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return  slow

    def noLoop(self, head1, head2):
        if head1 == None or head2 == None:
            return None

        cur1 = head1
        cur2 = head2
        n = 0
        while cur1.next is not None:
            n += 1
            cur1 = cur1.next

        while cur2.next is not None:
            n -= 1
            cur2 = cur2.next

        # 两个链表最后的节点不相等
        if cur1 != cur2:
            return None

        # 让head1作为较长的那一条链表
        if n < 0:
            head1, head2 = head2, head1
            n = abs(n)

        cur1 = head1
        cur2 = head2
        # 长的链表先走n步
        while n != 0:
            cur1 = cur1.next
            n -= 1

        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next

        return cur1

    def bothLoop(self, head1, loop1, head2, loop2):
        if loop1 == loop2:
            cur1 = head1
            cur2 = head2
            n = 0
            while cur1 != loop1:
                n += 1
                cur1 = cur1.next
            while cur2 != loop2:
                n -= 1
                cur2 = cur2.next
            if n < 0:
                head1, head2 = head2, head1
                n = abs(n)
            cur1 = head1
            cur2 = head2
            while n != 0:
                cur1 = cur1.next
                n -= 1
            while cur1 != cur2:
                cur1 = cur1.next
                cur2 = cur2.next
            return cur1
        else:
            #两个都有环，环上面必有两个链表的交点loop1 loop2，必定可以相遇；否则两链表无公共点
            cur1 = loop1.next
            while cur1 != loop1:
                if cur1 == loop2:
                    return loop1
                cur1 = cur1.next
            return None

    def getIntersectNode(self, head1, head2):
        if head1 == None or head2 == None:
            return None

        loop1 = self.getLoopNode(head1)
        loop2 = self.getLoopNode(head2)
        if loop1 == None and loop2 == None:
            return self.noLoop(head1, head2)
        elif loop1 is not None and loop2 is not None:
            return self.bothLoop(head1, loop1, head2, loop2)

        return None

if __name__ == '__main__':
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = Node(6)
    head1.next.next.next.next.next.next = Node(7)

    head2 = Node(0)
    head2.next = Node(9)
    head2.next.next = Node(8)
    head2.next.next.next = head1.next.next.next.next.next
    print('test1: ')
    print(FindeFirstIntersectNode().getIntersectNode(head1, head2).val)

    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = Node(6)
    head1.next.next.next.next.next.next = Node(7)
    head1.next.next.next.next.next.next.next = head1.next.next.next; # 7->4

    head2 = Node(0)
    head2.next = Node(9)
    head2.next.next = Node(8)

    head2.next.next.next = head1.next; # 8->2
    print('test2: ')
    print(FindeFirstIntersectNode().getIntersectNode(head1, head2).val)

    head2 = Node(0)
    head2.next = Node(9)
    head2.next.next = Node(8)
    head2.next.next.next = head1.next.next.next.next.next
    print('test3: ')
    print(FindeFirstIntersectNode().getIntersectNode(head1, head2).val)