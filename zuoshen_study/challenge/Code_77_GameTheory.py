class Solution(object):
    def __init__(self):
        return

    def f(self, arr, i, j):
        if i == j:
            return arr[i]
        return max(arr[i] + self.s(arr, i+1, j), arr[j] + self.s(arr, i, j-1))

    def s(self, arr, i, j):
        if i == j:
            return 0
        return min(self.f(arr, i+1, j), self.f(arr, i, j-1))

    def play_game(self, arr):
        if len(arr) == 0:
            return 0
        return max(self.f(arr, 0, len(arr)-1), self.s(arr, 0, len(arr)-1))

    def dps(self, arr):
        if len(arr) == 0:
            return 0
        n = len(arr)
        f = [[0 for i in range(n)] for j in range(n)]
        s = [[0 for i in range(n)] for j in range(n)]
        for j in range(n):
            f[j][j] = arr[j] # i == j
            s[j][j] = 0
            for i in range(j-1, -1, -1):
                f[i][j] = max(arr[i] + s[i+1][j], arr[j] + s[i][j-1])
                s[i][j] = min(f[i+1][j], f[i][j-1])
        return max(f[0][n-1], s[0][n-1])

if __name__ == '__main__':
    arr = [1, 2, 100, 4]
    res = Solution().play_game(arr)
    print(res)
    print('>>>>===============>>>>')
    res = Solution().dps(arr)
    print(res)
