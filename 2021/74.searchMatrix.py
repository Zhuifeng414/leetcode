class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i, j = 0, 0
        m, n = len(matrix), len(matrix[0])
        while i < m and j < n:
            print(i, j)
            if matrix[i][j] < target:
                if i+1 < m and matrix[i+1][j] < target:
                    i += 1
                else:
                    if j+1 < n:
                        j += 1
                    else:
                        i += 1
                        j = 0
            elif matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                return False
        return False

if __name__ == '__main__':
    matrix = [[1],[3]]
    target = 3
    print(Solution().searchMatrix(matrix, target))