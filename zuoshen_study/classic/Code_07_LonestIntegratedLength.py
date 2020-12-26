class Solution(object):
    def __init__(self):
        return

    def getLIL(self, arr):
        if len(arr) == 0:
            return 0
        res_len = 0
        for L in range(len(arr)):
            set_list = []
            max_v = -1e6
            min_v = 1e6
            for R in range(L, len(arr)):
                if arr[R] in set_list:
                    break
                set_list.append(arr[R])
                max_v = max(max_v, arr[R])
                min_v = min(min_v, arr[R])
                # max - min = 个数 - 1
                if max_v - min_v == R - L:
                    res_len = max(res_len, R-L+1)
        return res_len

if __name__ == '__main__':
    arr = [100, 5, 2, 1, 4, 1000]
    print(Solution().getLIL(arr))