class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix[0])
        if m % 2 == 1:
            n = (m+1) // 2
        else:
            n = m // 2
        for i in range(0, n+1):
            for j in range(0, m-1-2*i):
                p1 = [i, i+j]
                p2 = [i+j, m-1-i]
                p3 = [m-1-i, m-1-i-j]
                p4 = [m-1-i-j, i]
                self.singal_rote(p1, p2, p3, p4)

    def copy_matrix_point(self, v, p):
        matrix[p[0]][p[1]] = v

    def singal_rote(self, p1, p2, p3, p4):
        cache_p = matrix[p2[0]][p2[1]]
        self.copy_matrix_point(matrix[p1[0]][p1[1]], p2)
        cache_q = matrix[p3[0]][p3[1]]
        self.copy_matrix_point(cache_p, p3)
        cache_p = matrix[p4[0]][p4[1]]
        self.copy_matrix_point(cache_q, p4)
        self.copy_matrix_point(cache_p, p1)

if __name__ == '__main__':
    matrix = [
      [ 5, 1, 9,11],
      [ 2, 4, 8,10],
      [13, 3, 6, 7],
      [15,14,12,16]
    ]

    Solution().rotate(matrix)

    for item in matrix:
        print(item)
