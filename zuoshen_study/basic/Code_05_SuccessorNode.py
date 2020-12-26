class Node(object):
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class SuccessorNode():
    def __init__(self):
        return

    def getLeftMost(self, node):
        if node is None:
            return node
        while node.left is not None:
            node = node.left
        return node

    def getSuccessorNode(self, node):
        if node is None:
            return node

        if node.right is not None:
            return self.getLeftMost(node.right)
        else:
            parent = node.parent
            while parent is not None and parent.left != node:
                node = parent
                parent = node.parent
            return parent

if __name__ == '__main__':
    head = Node(6)
    head.parent = None
    head.left = Node(3)
    head.left.parent = head
    head.left.left = Node(1)
    head.left.left.parent = head.left
    head.left.left.right = Node(2)
    head.left.left.right.parent = head.left.left
    head.left.right = Node(4)
    head.left.right.parent = head.left
    head.left.right.right = Node(5)
    head.left.right.right.parent = head.left.right
    head.right = Node(9)
    head.right.parent = head
    head.right.left = Node(8)
    head.right.left.parent = head.right
    head.right.left.left = Node(7)
    head.right.left.left.parent = head.right.left
    head.right.right = Node(10)
    head.right.right.parent = head.right

    test = head.left.left
    print('getSuccessorNode: ', SuccessorNode().getSuccessorNode(test).val)

