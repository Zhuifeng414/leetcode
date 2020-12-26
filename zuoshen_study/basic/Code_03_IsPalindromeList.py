class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, item):
        self.stack.append(item) # 添加元素
        self.size += 1 # 栈元素数量加 1

    def pop(self):
        pop = self.stack.pop() # 删除栈顶元素
        self.size -= 1 # 栈元素数量减 1
        return pop

    def isEmpty(self):
        return self.stack == []

    def sizes(self):
        return self.size

    def peek(self):
        return self.stack[-1]

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

class IsPalindromeList():
    def __init__(self):
        return

    def isPalindrome_simple(self, head):
        stack = Stack()
        cur = head
        while cur is not None:
            stack.push(cur)
            cur = cur.next

        while head is not None:
            if head.val != stack.pop().val:
                return False
            head = head.next
        return True

    def isPalindrome_middle(self, head):
        if head is None or head.next is None:
            return True
        right = head.next
        cur = head
        while cur.next is not None and cur.next.next is not None:
            right = right.next
            cur = cur.next.next
        stack = Stack()
        while right is not None:
            stack.push(right)
            right = right.next
        while not stack.isEmpty():
            if head.val != stack.pop().val:
                return False
            head = head.next
        return True

    def isPalindrome_small(self, head):
        if head is None or head.next is None:
            return True

        n1 = head
        n2 = head
        while n2.next is not None and n2.next.next is not None:
            n1 = n1.next # n1 -> mid
            n2 = n2.next.next # n2 -> end

        # 将右侧反转
        n2 = n1.next
        n1.next = None
        n3 = None
        while n2 is not None:
            n3 = n2.next
            n2.next = n1
            n1 = n2
            n2 = n3

        n3 = n1 #右侧链表的头部
        n2 = head
        res = True
        while n1 is not None and n2 is not None:
            if n1.val != n2.val:
                res = False
                break
            n1 = n1.next #走到中点停止
            n2 = n2.next

        #恢复链表
        n1 = n3.next
        n3.next = None
        while n1 is not None:
            n2 = n1.next
            n1.next = n3
            n3 = n1
            n1 = n2

        return res



if __name__ == '__main__':
    print('isPalindrome:')
    node1 = ListNode(2)
    node1.next = ListNode(3)
    node1.next.next = ListNode(3)
    node1.next.next.next = ListNode(2)
    print('init list: ')
    node1.printLinkedList(node1)
    if IsPalindromeList().isPalindrome_small(node1):
        print('Yes!')
    else:
        print('Ooops ...')
    node1.printLinkedList(node1)
    print('the end')