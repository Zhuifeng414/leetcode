class PrintBinaryTree():
    def __init__(self):
        return

    def getSpace(self, num):
        space = " " * num
        return space

    def printInOrder(self, head, height, to, leng):
        if head is None:
            return
        self.printInOrder(head.right, height+1, 'v', leng)
        val = str(to) + str(head.val) + str(to)
        #print('val', val)
        lenM = len(str(val))
        lenL = int((leng - lenM) / 2)
        lenR = leng - lenM - lenL
        val = self.getSpace(lenL) + val + self.getSpace(lenR)
        print(self.getSpace(height * leng) + val)
        self.printInOrder(head.left, height+1, '^', leng)

    def printTree(self, head):
        print('Binary Tree')
        self.printInOrder(head, 0, "H", 17)
        return

class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialByPre(self, head):
        if head is None:
            return '#!'
        res = str(head.val) + '!'
        res += self.serialByPre(head.left)
        res += self.serialByPre(head.right)
        return res

    def reconPreOrder(self, queue):
        value = queue.pop(0)
        if value == '#':
            return None
        head = Node(value)
        head.left = self.reconPreOrder(queue)
        head.right = self.reconPreOrder(queue)
        return head

    def reconByPreStr(self, preStr):
        queue = [item for item in preStr.split('!') if len(item)>0]
        return self.reconPreOrder(queue)

    def serialByLevel(self, head):
        if head is None:
            return '#!'
        res = str(head.val) + '!'
        queue = []
        queue.append(head)
        while len(queue) > 0:
            head = queue.pop(0)
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

    def genNodeByStr(self, val):
        if val == '#':
            return None
        else:
            return Node(val)

    def reconByLevelStr(self, LevelStr):
        StrList = [item for item in LevelStr.split('!') if len(item)>0]
        index = 0
        head = self.genNodeByStr(StrList[index])
        index += 1
        queue = []
        if head is not None:
            queue.append(head)
        while len(queue) > 0:
            node = queue.pop(0)
            node.left = self.genNodeByStr(StrList[index])
            index += 1
            node.right = self.genNodeByStr(StrList[index])
            index += 1
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return head

    def morris(self, head, mode='pre'):
        if head is None:
            print('#!')
            return None
        cur = head
        mostRight = None
        while cur is not None:
            tmp = cur.left
            # have left sub tree
            if tmp is not None:
                # find mostRight
                # tmp.right != cur 避免进入死循环，单之前的 mostRight = cur的时候
                while tmp.right is not None and tmp.right != cur:
                    tmp = tmp.right
                mostRight = tmp
                # mostRight.right is null, mostRight.right to cur, cur to left
                if mostRight.right is None:
                    mostRight.right = cur
                    if mode == 'pre':
                        print(str(cur.val) + '!')
                    cur = cur.left # first time
                # mostRight.right = cur, mostRight.right to null, cur to right
                else:
                    mostRight.right = None
                    if mode == 'in':
                        print(str(cur.val) + '!')
                    cur = cur.right # second time
            else:
                # no left sub tree, cur move to right
                if mode == 'pre' or mode == 'in':
                    print(str(cur.val) + '!')
                cur = cur.right # only one time

if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.right.left = Node(6)
    head.right.right = Node(7)
    print('================>>>>')
    PrintBinaryTree().printTree(head)
    print('================>>>>')
    preStr = Node().serialByPre(head)
    print(preStr)
    print('pre ================>>>>')
    Node().morris(head, 'pre')
    print('in ================>>>>')
    Node().morris(head, 'in')



