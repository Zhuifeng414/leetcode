class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class IsBalanceTree():
    def __init__(self):
        return

    def ReturnData(self, isB, h):
        return {'isB': isB, 'b': h}

    def process(self, head):
        if head is None:
            return self.ReturnData(True, 0)

        leftData = self.process(head.left)
        if not leftData['isB']:
            return self.ReturnData(False, 0)
        rightData = self.process(head.right)
        if not rightData['isB']:
            return self.ReturnData(False, 0)
        if abs(leftData['h'] - rightData['h']) > 1:
            return self.ReturnData(False, 0)
        return self.ReturnData(True, max(leftData['h'], rightData['h'])+1)