class PreAndInArrayToPosArray(object):
    def __init__(self):
        return

    def get_sub(self, pre, mid, pos, L1, R1, L2, R2, L3, R3):
        if L1 > R1:
            return
        if L1 == R1:
            pos[L3] = pre[L1]
        pos[R3] = pre[L1]
        for find in range(L2, R2+1):
            if mid[find] == pre[L1]:
                break
        self.get_sub(pre, mid, pos, L1+1, find+L1-L2, L2, find-1, L3, find+L3-L2-1)
        self.get_sub(pre, mid, pos, find+L1-L2+1, R1, find+1, R2, find+L3-L2, R3-1)

    def getPosArray(self, pre, mid):
        if pre is None:
            return None
        if len(pre) != len(mid):
            return None
        N = len(pre)
        pos = [0 for i in range(N)]
        self.get_sub(pre, mid, pos, 0, N-1, 0, N-1, 0, N-1)
        return pos

if __name__ == '__main__':
    pre = [1, 2, 4, 5, 3, 6, 7]
    mid = [4, 2, 5, 1, 6, 3, 7]
    print(PreAndInArrayToPosArray().getPosArray(pre, mid))



