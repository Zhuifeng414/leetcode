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

class GetMinStack:
    def __init__(self):
        self.stackData = Stack()
        self.stackMin = Stack()
        return

    def getmin(self):
        if self.stackMin.isEmpty():
            print('Your min_stack is empty !')
            return
        return self.stackMin.peek()


    def push(self, newNum):
        ## push最小栈
        if self.stackMin.isEmpty():
            self.stackMin.push(newNum)
        elif self.getmin() > newNum:
            self.stackMin.push(newNum)
        else:
            self.stackMin.push(self.getmin())
        ## push存储栈
        self.stackData.push(newNum)

    def pop(self):
        if self.stackData.isEmpty():
            print('Your data stack is empty !')
            return
        self.stackMin.pop()
        return self.stackData.pop()

if __name__ == '__main__':
    stack1 = GetMinStack()
    stack1.push(3)
    stack1.push(4)
    stack1.push(1)
    print(stack1.getmin())
    print(stack1.pop())
    print(stack1.getmin())




