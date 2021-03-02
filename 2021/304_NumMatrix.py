class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] += (matrix[i][j-1] if j-1>=0 else 0) \
                                + (matrix[i-1][j] if i-1>=0 else 0) \
                                - (matrix[i-1][j-1] if i-1>=0 and j-1>=0 else 0)
        self.matrix = matrix

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        lu = [row1, col1]
        ru = [row1, col2]
        ld = [row2, col1]
        rd = [row2, col2]
        res = self.matrix[rd[0]][rd[1]] \
              - (self.matrix[ld[0]][ld[1]-1] if ld[1]-1>=0 else 0) \
              - (self.matrix[ru[0]-1][ru[1]] if ru[0]-1>=0 else 0) \
              + (self.matrix[lu[0]-1][lu[1]-1] if lu[0]-1>=0 and lu[1]-1>=0 else 0)
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == '__main__':
    matrix = [[0, 1, 1, 5],
              [2, 3, 4, 1],
              [0, 1, 1, -1],
              [2, 1, -1, -2]]
    #print(NumMatrix(matrix).matrix)
    print(NumMatrix(matrix).sumRegion(1, 1, 3, 3))
