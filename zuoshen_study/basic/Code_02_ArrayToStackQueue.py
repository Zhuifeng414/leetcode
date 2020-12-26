class ArrayToStack:
    def __init__(self):
        self.arr = []
        self.size = 0
        return

    def ArrayStack(self, initSize):
        if initSize < 0:
            print('The init size is less than 0')
        self.arr = [-1]*initSize
        self.size = 0

    def peek(self):
        if self.size == 0:
            return None
        return self.arr(self.size - 1)

    def push(self, obj):
        if self.size >= len(self.arr):
            print('The stack is full!')
        self.arr[self.size] = obj
        self.size += 1

    def pop(self):
        if self.size == 0:
            print('The stack is empty!')
        self.size -= 1
        return self.arr[self.size]


class ArrayToQueue:
    def __init__(self):
        self.arr = []
        self.size = 0
        self.first = 0
        self.last = 0

    def ArrayQueue(self, initSize):
        if initSize < 0:
            print('The init size is less than 0')
        self.arr = [0]*initSize
        self.size = 0
        self.first = 0
        self.last = 0
        return

    def peek(self):
        if self.size == 0:
            return None
        return self.arr[self.first]

    def push(self, obj):
        if self.last >= self.size:
            print('The queue is full !')
        self.size += 1
        self.arr[self.last] = obj
        self.last = 0 if self.last == len(self.arr) - 1 else self.last + 1

    def poll(self):
        if self.size == 0:
            return print('The queue is empty !')
        self.size -= 1
        tmp = self.first
        self.first = 0 if self.first == len(self.arr) - 1 else self.first + 1
        return self.arr[tmp]

if __name__ == '__main__':
    print('Hello world !')