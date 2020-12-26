import random
import numpy as np

class RotateMatrix:
    def __init__(self):
        return

    def rotateEdge(self, m, tR, tC, dR, dC):
        times = dC - tC
        for i in range(times):
            tmp = m[tR][tC + i]
            m[tR][tC + i] = m[dR - i][tC]
            m[dR - i][tC] = m[dR][dC - i]
            m[dR][dC - i] = m[tR + i][dC]
            m[tR + i][dC] = tmp
        return
            
    def rotate(self, m):
        tR = 0
        tC = 0
        dR = len(m) - 1
        dC = len(m[0]) - 1
        while tR < dR:
            self.rotateEdge(m, tR, tC, dR, dC)
            tR += 1
            tC += 1
            dR -= 1
            dC -= 1
        return m

    def printMatrix(self, m):
        for item in m:
            print(item)
    
class ComparatorsTool:
    def __init__(self):
        # do nothing
        return

    def flip90_right(self, arr):
        new_arr = arr.reshape(arr.size)
        new_arr = new_arr[::-1]
        new_arr = new_arr.reshape(arr.shape)
        new_arr = np.transpose(new_arr)[::-1]
        return new_arr

    # 一种简单 好实现的准确方法
    def comparator(self, arr):
        res = self.flip90_right(np.array(arr))
        return res.tolist()

    # 随机Matrix生成器
    def generateRandomMatrix(self, maxSize, maxValue):
        arr = []
        size = max(1, int(random.random()*(maxSize+1)))
        for i in range(size):
            sub_arr = []
            for i in range(size):
                value = int(random.random()*(maxValue+1)) #- int(random.random()*(maxValue))
                sub_arr.append(value)
            arr.append(sub_arr)
        return arr

    # 复制Matrix
    def copyMatrix(self, arr):
        res = [[0 for j in range(len(arr[0]))] for i in range(len(arr))]
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                res[i][j] = arr[i][j]
        return res

    # 比较两个Matrix是否相等
    def isEqual(self, res1, res2):
        if len(res1) == len(res2) and len(res1[0]) == len(res2[0]):
            for i in range(len(res1)):
                for j in range(len(res1[0])):
                    if res1[i][j] == res2[i][j]:
                        continue
                    else:
                        return False
            return True
        else:
            return False

    def printArray(self, arr):
        for item in arr:
            print(item)
            
if __name__ == '__main__':
    testTimes = 200
    maxSize = 10
    maxValue = 9
    flag = True
    cmp = ComparatorsTool()
    rtm = RotateMatrix()
    for i in range(testTimes):
        arr = cmp.generateRandomMatrix(maxSize, maxValue)
        arr1 = cmp.copyMatrix(arr)
        arr2 = cmp.copyMatrix(arr)
        res1 = cmp.comparator(arr1)
        res2 = rtm.rotate(arr2)
        if cmp.isEqual(res1, res2):
            continue
        else:
            flag = False
            print('Ooops !')
            print('init############')
            rtm.printMatrix(arr)
            print('res1############')
            rtm.printMatrix(res1)
            print('res2############')
            rtm.printMatrix(res2)
    if flag:
        print('Nice ! ')
