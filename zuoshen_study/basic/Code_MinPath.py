class MinPath():
    def __init__(self):
        return

    def process_min_path(self, matrix, i, j):
        res = matrix[i][j]
        if i == len(matrix)-1 and j == len(matrix[0])-1:
            return res

        if i == len(matrix)-1 and j < len(matrix[0])-1:
            return res + self.process(matrix, i, j+1)

        if i < len(matrix)-1 and j == len(matrix[0])-1:
            return res + self.process(matrix, i+1, j)

        return res + min(self.process(matrix, i+1, j), self.process(matrix, i, j+1))




if __name__ == '__main__':
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [9, 8, 7]
    ]
    print(MinPath().process_min_path(m, 0, 0))