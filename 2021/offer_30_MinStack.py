class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []
        self.B = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.A.append(x)
        if len(self.B) == 0 or self.B[-1] >= x:
            self.B.append(x)


    def pop(self):
        """
        :rtype: None
        """
        if self.A.pop() == self.B[-1]:
            self.B.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.A[-1]


    def min(self):
        """
        :rtype: int
        """
        return self.B[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()