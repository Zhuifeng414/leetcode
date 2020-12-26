# 树
class Node(object):
    def __init__(self, val=0, left=None ,right=None):
        self.val = val
        self.left = left
        self.right = right
# 队列
class Queue:
    def __init__(self):
        self.arr = []
        self.size = 0
        self.first = 0
        self.last = 0

    def push(self, obj):
        self.size += 1
        self.arr.append(obj)
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
        return self.size == 0

    def sizes(self):
        return self.size

## 打印二叉树
class PrintBinaryTree():
    def __init__(self):
        return

    def getSpace(self, num):
        space = " " * num
        return space

    def printInOrder(self, head, height, to, leng):
        if head is None:
            return
        self.printInOrder(head.right, height + 1, 'v', leng)
        val = str(to) + str(head.val) + str(to)
        # print('val', val)
        lenM = len(str(val))
        lenL = int((leng - lenM) / 2)
        lenR = leng - lenM - lenL
        val = self.getSpace(lenL) + val + self.getSpace(lenR)
        print(self.getSpace(height * leng) + val)
        self.printInOrder(head.left, height + 1, '^', leng)

    def printTree(self, head):
        print('Binary Tree')
        self.printInOrder(head, 0, "H", 17)
        return

# 序列化和反序列化
class SerializeAndReconstructTree:
    def __init__(self):
        return

    def serialByPre(self, head):
        if head is None:
            return '#!'
        res = str(head.val) + '!'
        res += self.serialByPre(head.left)
        res += self.serialByPre(head.right)
        return res

    def reconPreOrder(self, queue):
        value = queue.poll()
        if value == '#':
            return None
        head = Node(value)
        head.left = self.reconPreOrder(queue)
        head.right = self.reconPreOrder(queue)
        return head

    def reconByPreString(self, preStr):
        values = preStr.split('!')
        queue = Queue()
        for i in range(len(values)):
            queue.push(values[i])
        return self.reconPreOrder(queue)

    def serialByLevel(self, head):
        if head is None:
            return '#!'
        res = str(head.val) + '!'
        queue = []
        queue.append(head)
        while len(queue) > 0:
            head = queue.pop()
            if head.left is not None:
                res += str(head.left.val) + '!'
                queue.append(head.left)
            else:
                res += '#!'
            if head.right is not None:
                res += str(head.right.val) + '!'
                queue.append(head.right)
            else:
                res += '#!'
        return res

    def generateNodeByString(self, val):
        if val == '#':
            return None
        return Node(int(val))

    def reconByLevelString(self, levelStr):
        values = levelStr.split('!')
        index = 0
        head = self.generateNodeByString(values[index])
        index += 1
        queue = []
        if head is not None:
            queue.append(head)
        while len(queue) > 0:
            node = queue.pop()
            node.left = self.generateNodeByString(values[index])
            index += 1
            node.right = self.generateNodeByString(values[index])
            index += 1
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return head

if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.right.right = Node(5)
    PrintBinaryTree().printTree(head)
    print('==================================')

    pre = SerializeAndReconstructTree().serialByPre(head)
    print("serialize tree by pre-order: " + pre)
    head = SerializeAndReconstructTree().reconByPreString(pre)
    print("reconstruct tree by pre-order, ")
    PrintBinaryTree().printTree(head)

    level = SerializeAndReconstructTree().serialByLevel(head)
    print("serialize tree by level: " + level)
    head = SerializeAndReconstructTree().reconByLevelString(level)
    print("reconstruct tree by level, ")
    PrintBinaryTree().printTree(head)



