class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if i+1 < m and j+1 < n:
                    if matrix[i][j] == matrix[i+1][j+1]:
                        continue
                    else:
                        return False
        return True
