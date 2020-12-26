import random


# 数组的小和问题
class AllNotInclude:

    def __init__(self):
        # do nothing
        return

    def getAllNotInclude(self, arr1, arr2): # arr2 已经排好顺序
        res = []
        for i in range(len(arr1)):
            l = 0
            r = len(arr2) - 1
            contain = False
            while(l <= r):
                mid = int((l+r)/2)
                if arr2[mid] == arr1[i]:
                    contain = True
                    break
                elif arr2[mid] > arr1[i]:
                    r = mid - 1
                else:
                    l = mid + 1
            if not contain:
                res.append(arr1[i])
        return res


class ComparatorsTool:
    def __init__(self):
        # do nothing
        return

    # 一种简单 好实现的准确方法
    def comparator(self, arr1, arr2):
        res = []
        for v_i in arr1:
            if v_i not in arr2:
                res.append(v_i)
        return res

    # 随机list生成器
    def generateRandomArray(self, maxSize, maxValue):
        arr = []
        size = int(random.random() * (maxSize + 1))
        for i in range(size):
            # value = int(random.random()*(maxValue+1)) - int(random.random()*(maxValue))
            value = int(random.random() * (maxValue + 1))
            arr.append(value)
        return arr

    # 复制Array
    def copyArray(self, arr):
        res = [item for item in arr]
        return res

    # 比较两个Array是否相等
    def isEqual(self, res1, res2):
        if len(res1) == len(res1):
            for i in range(len(res1)):
                if res1[i] != res2[i]:
                    return False
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
    sortLib = AllNotInclude()
    cmpt = ComparatorsTool()
    for i in range(testTime):
        arr_a = cmpt.generateRandomArray(maxSize, maxValue)
        arr_b = cmpt.generateRandomArray(maxSize, maxValue)
        arr_b.sort()
        print('############')
        print(arr_a)
        print(arr_b)
        print('############')
        arr1 = cmpt.copyArray(arr_a)
        arr2 = cmpt.copyArray(arr_a)
        res1 = sortLib.getAllNotInclude(arr_a, arr_b)
        res2 = cmpt.comparator(arr_a, arr_b)
        if not cmpt.isEqual(res1, res2):
            succeed = False
            break
    if succeed:
        print('Nice!')
    else:
        print('Fucking fucked!')


