class ZigZagPrintMatrix():
    def __init__(self):
        # do nothing
        return

    def printLevel(self, m, tR, tC, dR, dC, flag):
        if flag: #从上往下
            while dC >= tC:
                print(m[dR][dC])
                dR += 1
                dC -= 1
        else: #从下往上
            while tC <= dC:
                print(m[tR][tC])
                tR -= 1
                tC += 1
        return

    def printMatrixZigZag(self, m):
        tR = 0
        tC = 0
        dR = 0
        dC = 0
        endR = len(m) - 1
        endC = len(m[0]) - 1
        flag = False #先从下往上
        while tC != endC + 1:
            #print('index', tR, tC, dR, dC, flag)
            self.printLevel(m, tR, tC, dR, dC, flag)
            dR = dR + 1 if dC == endC else dR
            dC = dC if dC == endC else dC + 1
            tC = tC + 1 if tR == endR else tC
            tR = tR if tR == endR else tR + 1
            flag = not flag


if __name__ == '__main__':
    test = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    ZigZagPrintMatrix().printMatrixZigZag(test)
    print('end')
    #ZigZagPrintMatrix().printLevel(test, 2, 0, 0, 2, True)



