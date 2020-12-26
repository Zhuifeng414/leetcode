class PrintMatrixSpiralOrder():
    def __init__(self):
        # do nothing
        return

    def printEdge(self, m, tR, tC, dR, dC):
        if(tR == dR):
            for i in range(tC, dC + 1):
                print(m[tR][i])
        elif(tC == dC):
            for i in range(tR, dR + 1):
                print(m[i][tC])
        else:
            curR = tR
            curC = tC
            while curC != dC:
                print(m[tR][curC])
                curC += 1
            while curR != dR:
                print(m[curR][dC])
                curR += 1
            while curC != tC:
                print(m[dR][curC])
                curC -= 1
            while curR != tR:
                print(m[curR][tC])
                curR -= 1
        return

    def spiralOrderPrint(self, m):
        tR = 0
        tC = 0
        dR = len(m) - 1
        dC = len(m[0]) - 1
        while tR <= dR and tC <= dC:
            self.printEdge(m, tR, tC, dR, dC)
            tR += 1
            tC += 1
            dR -= 1
            dC -= 1

if __name__ == '__main__':
    test = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    PrintMatrixSpiralOrder().spiralOrderPrint(test)