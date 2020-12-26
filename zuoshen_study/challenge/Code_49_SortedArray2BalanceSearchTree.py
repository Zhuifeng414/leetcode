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

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        return

    def process(self, arr, L, R):
        if L > R:
            return None
        mid = int((L + R)/2)
        head = Node(arr[mid])
        head.left = self.process(arr, L, mid-1)
        head.right = self.process(arr, mid+1, R)
        return head


if __name__ == '__main__':
   arr = [1, 2, 3, 4, 5]
   head = Solution().process(arr, 0, len(arr)-1)
   PrintBinaryTree().printTree(head)