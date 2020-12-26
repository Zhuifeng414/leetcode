class Employee(object):
    def __init__(self, happy=0, subordinates=[]):
        self.happy = happy
        self.subordinates = subordinates

class Info(object):
    def __init__(self, yesHeadMax, noHeadMax):
        self.yesHeadMax = yesHeadMax
        self.noHeadMax = noHeadMax

class Solution(object):
    def __init__(self):
        return

    def process(self, head):
        yesX = head.happy
        noX = 0
        if len(head.subordinates) == 0:
            return Info(yesX, noX)
        for next in head.subordinates:
            subInfo = self.process(next)
            yesX += subInfo.noHeadMax
            noX += max(subInfo.yesHeadMax, subInfo.noHeadMax)
        return Info(yesX, noX)