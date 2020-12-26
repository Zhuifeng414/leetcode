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
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        return

class Solution(object):
    def __init__(self):
        return

    def isPost(self, arr, start, end):
        if start == end:
            return True
        less = -1
        more = end
        for i in range(start, end):
            if arr[i] < arr[end]:
                # change every time
                less = i
            else:
                # only change once
                more = i if more == end else more

        if less == -1 or more == end:
            return self.isPost(arr, start, end-1)
        if more - less != 1:
            return False

        return self.isPost(arr, start, less) \
                and self.isPost(arr, more, end-1)

    def constructPostTree(self, arr, start, end):
        if start > end:
            return None
        less = -1
        more = end
        head = Node(arr[end])
        for i in range(start, end):
            if arr[i] < arr[end]:
                # change every time
                less = i
            else:
                # only change once
                more = i if more == end else more

        head.left = self.constructPostTree(arr, start, less)
        head.right = self.constructPostTree(arr, more, end - 1)
        return head

if __name__ == '__main__':
    arr = [1, 3, 2, 6, 8, 7, 4]
    head = Solution().constructPostTree(arr, 0, len(arr)-1)
    PrintBinaryTree().printTree(head)