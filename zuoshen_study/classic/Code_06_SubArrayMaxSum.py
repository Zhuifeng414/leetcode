class Solution(object):
    def __init__(self):
        return

    def process(self, arr, sum_res, index):
        if index > len(arr) - 1:
            return sum_res
        p1 = self.process(arr, sum_res + arr[index], index+1)
        p2 = self.process(arr, sum_res, index+1)
        return max(p1, p2)

    def max_sum_arr(self, arr):
        if len(arr) == 0:
            return 0

        max_res = -999
        cur = 0
        for i in range(len(arr)):
            cur += arr[i]
            max_res = max(max_res, cur)
            cur = 0 if cur < 0 else cur
        return max_res

    def max_sum_matrix(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        max_res = -999
        cur = 0
        for i in range(len(matrix)):
            s = [0 for i in range(len(matrix[0]))]
            for j in range(i, len(matrix)):
                cur = 0
                for k in range(len(matrix[0])):
                    s[k] += matrix[j][k]
                    cur += s[k]
                    max_res = max(max_res, cur)
                    cur = 0 if cur < 0 else cur
        return max_res

if __name__ == '__main__':
    # arr = [-1, -2, -3, -2, -3, -7, -3]
    # print(Solution().max_sum_arr(arr))
    matrix = [
        [-90, 48, 78],
        [64, -40, 64],
        [-81, -7, 66]
    ]
    print(Solution().max_sum_matrix(matrix))