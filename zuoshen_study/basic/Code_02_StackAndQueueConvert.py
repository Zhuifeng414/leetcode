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

class Queue:
    def __init__(self):
        self.arr = []
        self.size = 0
        self.first = 0
        self.last = 0

    def push(self, obj):
        self.size += 1
        self.arr[self.last] = obj
        self.last = 0 if self.last == len(self.arr) - 1 else self.last + 1

    def peek(self):
        if self.size == 0:
            return None
        return self.arr[self.first]

    def poll(self):
        if self.size == 0:
            return print('The queue is empty !')
        self.size -= 1
        tmp = self.first
        self.first = 0 if self.first == len(self.arr) - 1 else self.first + 1
        return self.arr[tmp]

    def isEmpty(self):
        return self.arr == []

    def sizes(self):
        return self.size

class TwoStacksQueue:
    def __init__(self):
        self.stackPush = Stack()
        self.stackPop = Stack()
        return

    # 压入数据到队列
    def push(self, pushInt):
        self.stackPush.push(pushInt)

    # 弹出数据
    def poll(self):
        if self.stackPop.isEmpty() and self.stackPush.isEmpty():
            print('Queue is empty !')
        elif self.stackPop.isEmpty():
            while not self.stackPush.isEmpty():
                self.stackPop.push(self.stackPush.pop())
        return self.stackPop.pop()

    # 读取队列头部数据
    def peek(self):
        if self.stackPop.isEmpty() and self.stackPush.isEmpty():
            print('Queue is empty !')
        elif self.stackPop.isEmpty():
            while not self.stackPush.isEmpty():
                self.stackPop.push(self.stackPush.pop())
        return self.stackPop.peek()

class TwoQueuesStack:
    def __init__(self):
        self.queue = Queue()
        self.help = Queue()
        return

    def push(self, pushInt):
        self.queue.push(pushInt)
        return

    def swap(self):
        tmp = self.help
        self.help = self.queue
        self.queue = tmp
        return

    def peek(self):
        if self.queue.isEmpty():
            print('Queue is empty !')
        while self.queue.sizes() > 1:
            self.help.push(self.queue.poll())
        res = self.queue.poll()
        self.help.push(res)
        self.swap()
        return res

    def pop(self):
        if self.queue.isEmpty():
            print('Queue is empty !')
        while self.queue.sizes() > 1:
            self.help.push(self.queue.poll())
        res = self.queue.poll()
        self.swap()
        return res





