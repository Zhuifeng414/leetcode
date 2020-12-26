class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

class Info(object):
    def __init__(self, height=0):
        self.height = height

class PosArrayToBST(object):
    def __init__(self):
        return

    def findIndex(self, arr, L, R):
        value = arr[R]
        left = L
        right = R - 1
        mid = int((left + right)/2)
        if arr[mid] < value and arr[mid + 1] < value:
            L = mid
        if arr[mid] > value and arr[mid - 1] > value:
            R = mid
        if arr[mid] < value and arr[mid + 1] > value:
            return mid
        if arr[mid] > value and arr[mid - 1] < value:
            return mid - 1

        return self.findIndex(arr, arr, L, R)


    def process(self, arr, L, R):
        if len(arr) == 0:
            return None
        if L > R:
            return None
        head = Node(arr[R])
        if L == R:
            return head

        find = self.findIndex(arr, L, R)

        head.left = self.process(arr, L, find)
        head.right = self.process(arr, find+1, R-1)
        return head


    def getRes(self, arr):
       return self.process(arr, 0, len(arr)-1)



if __name__ == '__main__':
    arr = [1, 3, 2, 6, 8, 7, 5]
    head = PosArrayToBST().getRes(arr)
    PrintBinaryTree().printTree(head)
