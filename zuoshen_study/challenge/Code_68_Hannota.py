class Solution(object):
    def __init__(self):
        return

    def process(self, n, frm, mid, to):
        if n == 1:
            print('move from %s to %s'%(frm, to))
            return
        else:
            self.process(n-1, frm, to, mid)
            self.process(1, frm, mid, to)
            self.process(n-1, mid, frm, to)
            return

    def NB_process(self, arr, i, frm, mid, to):
        if i == -1:
            return 0
        if arr[i] != frm and arr[i] != to:
            return -1
        if arr[i] == frm:
            return self.NB_process(arr, i-1, frm, to, mid)
        else:
            rest = self.NB_process(arr, i-1, mid, frm, to)
            if rest == -1:
                return -1
            return (1 << i) + rest

    def NB_process_fast(self, arr):
        if len(arr) == 0:
            return -1
        frm = 1
        mid = 2
        to = 3
        i = len(arr) - 1
        res = 0
        tmp = 0
        while i >= 0:
            if(arr[i] != frm and arr[i] != to):
                return -1
            if arr[i] == frm: # see what will happend  i-1 frm-->mid
                mid, to = to, mid
            else:
                res += (1 << i)
                frm, mid = mid, frm # i-1 mid-->to
            i -= 1
        return res

    def NB_step(self, arr):
        if len(arr) == 0:
            return -1
        return self.NB_process(arr, len(arr)-1, 1, 2, 3)

if __name__ == '__main__':
    # n = 3
    # print(Solution().process(n, 'A', 'B', 'C'))
    arr = [2, 2]
    print(Solution().NB_step(arr))
    print('====================>>>')
    print(Solution().NB_process_fast(arr))