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

class Info(object):
    def __init__(self, psum, h):
        self.psum = psum
        self.h = h

class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def process(self, head, aim, psum, h):
        #print(psum, h)
        if head is None:
            return -1
        if psum + head.val == aim:
            return h+1
        h1 = self.process(head.left, aim, psum+head.val, h+1)
        h2 = self.process(head.left, aim, 0, 0)
        h3 = self.process(head.right, aim, psum+head.val, h+1)
        h4 = self.process(head.right, aim, 0, 0)
        return max(max(h1, h2), max(h3, h4))

    def preOrderMethod(self, head, aim, psum, level, max_len, sum_map):
        if head is None:
            return max_len
        cur_sum = psum + head.val
        if cur_sum not in sum_map.keys():
            sum_map[cur_sum] = level
        if cur_sum - aim in sum_map.keys():
            max_len = max(max_len, level - sum_map[cur_sum - aim])
        max_len = self.preOrderMethod(head.left, aim, cur_sum, level+1, max_len, sum_map)
        max_len = self.preOrderMethod(head.right, aim, cur_sum, level+1, max_len, sum_map)
        if level == sum_map[cur_sum]:
            sum_map.pop(cur_sum)
        return max_len

    def preOrderMaxLen(self, head, aim):
        sum_map = {0:0}
        return self.preOrderMethod(head, aim, 0, 1, 0, sum_map)


if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.right.left = Node(6)
    head.right.right = Node(7)
    aim = 10
    print('================>>>>')
    PrintBinaryTree().printTree(head)
    print('================>>>>')
    print(Node().process(head, aim, 0, 0))
    print('================>>>>')
    res = Node().preOrderMaxLen(head, aim)
    print(res)

