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

class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        return

    # mid left right
    def preOrderRecur(self, head):
        if head is None:
            return
        print(head.val)
        self.preOrderRecur(head.left)
        self.preOrderRecur(head.right)

    # left mid right
    def inOrderRecur(self, head):
        if head is None:
            return
        self.inOrderRecur(head.left)
        print(head.val)
        self.inOrderRecur(head.right)

    # left right mid
    def posOrderRecur(self, head):
        if head is None:
            return
        self.posOrderRecur(head.left)
        self.posOrderRecur(head.right)
        print(head.val)

    def preOrderUnRecur(self, head):
        if head is not None:
            stack = Stack()
            stack.push(head)
            while not stack.isEmpty():
                head = stack.pop()
                print(head.val)
                if head.right is not None:
                    stack.push(head.right)
                if head.left is not None:
                    stack.push(head.left)
        return

    def inOrderUnRecur(self, head):
        if head is not None:
            stack = Stack()
            while (not stack.isEmpty()) or (head is not None):
                if head is not None:
                    stack.push(head)
                    head = head.left
                else:
                    head = stack.pop()
                    print(head.val)
                    head = head.right
            return

    def posOrderUnRecur(self, head):
        if head is not None:
            s1 = Stack()
            s2 = Stack()
            s1.push(head)
            while not s1.isEmpty():
                head = s1.pop()
                s2.push(head.val)
                if head.left is not None:
                    s1.push(head.left)
                if head.right is not None:
                    s1.push(head.right)
            while not s2.isEmpty():
                print(s2.pop())
            return


