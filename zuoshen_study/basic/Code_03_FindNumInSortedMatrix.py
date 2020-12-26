class FindNumInSortedMatrix:
    def __init__(self):
        return

    def isContains(self, m, Knum):
        row = 0
        col = len(m[0]) - 1
        while row < len(m) and col > -1:
            if m[row][col] == Knum:
                return [True, row, col]
            elif m[row][col] < Knum:
                row += 1
            else:
                col -= 1
        return False

if __name__ == '__main__':
    test = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    res = FindNumInSortedMatrix().isContains(test, 9)
    if res[0]:
        print('find', res)
    else:
        print('Ooops!')
