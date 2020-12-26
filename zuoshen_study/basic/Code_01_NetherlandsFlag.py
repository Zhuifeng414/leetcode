import random
# 数组的小和问题
class Flag:

    def __init__(self):
        # do nothing
        return

    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

    def partition(self, arr, l, r, p):
        less = l - 1
        more = r + 1
        cur = l
        while(cur < more):
            if arr[cur] < p:
                less += 1
                self.swap(arr, less, cur)
                cur += 1
            elif arr[cur] > p:
                more -= 1
                self.swap(arr, cur, more)
            else:
                cur += 1
        return [less + 1, more - 1]
    




class ComparatorsTool:
    def __init__(self):
        # do nothing
        return

    # 一种简单 好实现的准确方法
    def comparator(self, arr, l, r, p):
        ts = arr.copy()
        index = l
        p_res = [-1, -1]
        for i in range(l, r+1):
            if arr[i] < p:
                ts[index] = arr[i]
                index += 1
        p_res[0] = index
        for i in range(l, r+1):
            if arr[i] == p:
                ts[index] = arr[i]
                index += 1
        p_res[1] = index - 1
        for i in range(l, r+1):
            if arr[i] > p:
                ts[index] = arr[i]
                index += 1
        return p_res

    # 随机list生成器
    def generateRandomArray(self, maxSize, maxValue):
        arr = []
        size = int(random.random()*(maxSize+1))
        for i in range(size):
            #value = int(random.random()*(maxValue+1)) - int(random.random()*(maxValue))
            value = int(random.random() * (maxValue + 1))
            arr.append(value)
        return arr

    # 复制Array
    def copyArray(self, arr):
        res = [item for item in arr]
        return res

    # 比较两个Array是否相等
    def isEqual(self, res1, res2):
        if res1[0] == res2[0] and res1[1] == res2[1]:
            return True
        else:
            return False

    def printArray(self, arr):
        for item in arr:
            print(item, ' ')


if __name__ == '__main__':
    testTime = 5
    maxSize = 10
    maxValue = 10
    succeed = True
    sortLib = Flag()
    cmpt = ComparatorsTool()
    for i in range(testTime):
        arr = cmpt.generateRandomArray(maxSize, maxValue)
        print('############')
        print(arr)
        arr1 = cmpt.copyArray(arr)
        arr2 = cmpt.copyArray(arr)
        res1 = sortLib.partition(arr1, 0, len(arr1)-1, arr1[0])
        res2 = cmpt.comparator(arr2, 0, len(arr2)-1, arr2[0])
        if not cmpt.isEqual(res1, res2):
            succeed = False
            break
    if succeed:
        print('Nice!')
    else:
        print('Fucking fucked!')
        print('arr', arr)
        print('arr1', res1, arr1)
        print('arr2', res2, arr2)

