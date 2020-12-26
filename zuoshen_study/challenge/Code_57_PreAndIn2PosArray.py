class Solution(object):
    def __init__(self):
        return

    def process(self, pre, mid, pos, L1, R1, L2, R2, L3, R3):
        if L1 > R1:
            return None
        if L1 == R1:
            pos[L3] = pre[L1]
        pos[R3] = pre[L1]
        for index in range(L2, R2+1):
            if mid[index] == pre[L1]:
                break
        self.process(pre, mid, pos, L1+1, L1+index-L2, L2, index-1, L3, L3+index-L2-1)
        self.process(pre, mid, pos, L1+index-L2+1, R1, index+1, R2, L3+index-L2, R3-1)

    def getPosArray(self, pre, mid):
        if len(pre) == 0 or len(pre) != len(mid):
            return None
        N = len(pre)
        pos = [0 for i in range(N)]
        self.process(pre, mid, pos, 0, N-1, 0, N-1, 0, N-1)
        return pos

if __name__ == '__main__':
    pre = [1, 2, 4, 5, 3, 6, 7]
    mid = [4, 2, 5, 1, 6, 3, 7]
    # [4, 5, 2, 6, 7, 3, 1]
    print(Solution().getPosArray(pre, mid))

