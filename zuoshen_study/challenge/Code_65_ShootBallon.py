class Solution(object):
    def __init__(self):
        return

    def process(self, arr, L, R):
        if L == R:
            return arr[L-1] * arr[L] * arr[R+1]
        p1 = arr[L-1] * arr[L] * arr[R+1] + self.process(arr, L+1, R)
        p2 = arr[L-1] * arr[R] * arr[R+1] + self.process(arr, L, R-1)
        max_v = max(p1, p2)
        for i in range(L+1, R):
            p3 = arr[L-1] * arr[i] * arr[R+1] \
                 + self.process(arr, L, i-1) \
                 + self.process(arr, i+1, R)
            max_v = max(max_v, p3)
        return max_v

if __name__ == '__main__':
    arr = [3, 2, 5]
    help = [1] + arr + [1]
    n = len(arr)
    print(Solution().process(help, 1, 3))