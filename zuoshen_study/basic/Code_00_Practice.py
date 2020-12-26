import random
# 数组的小和问题
class MySortLib:

    def __init__(self):
        # do nothing
        return

    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

    # 归并排序
    def mergeSort(self, arr):
        if len(arr) < 2:
            return sum(arr)
        return self.merge_sort(arr, 0, len(arr)-1)

    def merge_sort(self, arr, l, r):
        if l == r:
            return 0
        mid = (l + r)//2
        #print('merge_sort', arr, l, mid, r)
        return self.merge_sort(arr, l, mid) + \
        self.merge_sort(arr, mid+1, r) + \
        self.merge(arr, l, mid, r)


    def merge(self, arr, l, m, r):
        help = [0]*(r - l + 1)
        i = 0
        p1 = l
        p2 = m + 1
        res = 0
        while p1 <= m and p2 <= r:
            if arr[p1] < arr[p2]:
                res += arr[p1] * (r - p2 + 1)
                for k in range(p2, r+1):
                    print('(%s, %s)'%(arr[p1], arr[k]))
                help[i] = arr[p1]
                i += 1
                p1 += 1
            else:
                help[i] = arr[p2]
                i += 1
                p2 += 1

        if p1 <= m: # p2为空
            for k in range(p1, m+1):
                help[i] = arr[k]
                i += 1

        if p2 <= r: # p1为空
            for k in range(p2, r+1):
                help[i] = arr[k]
                i += 1

        for i in range(0, r - l + 1):
            arr[l+i] = help[i]
        return res

class ComparatorsTool:
    def __init__(self):
        # do nothing
        return

    # 一种简单 好实现的准确方法
    def comparator(self, arr):
        if len(arr) < 2:
            return sum(arr)
        res = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] < arr[j]:
                    res += arr[i]
        arr.sort()
        return res

    # 随机list生成器
    def generateRandomArray(self, maxSize, maxValue):
        arr = []
        size = int(random.random()*(maxSize+1))
        for i in range(size):
            value = int(random.random()*(maxValue+1)) - int(random.random()*(maxValue))
            arr.append(value)
        return arr

    # 复制Array
    def copyArray(self, arr):
        res = [item for item in arr]
        return res

    # 比较两个Array是否相等
    def isEqual(self, res1, res2):
        if res1 == res2:
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
    sortLib = MySortLib()
    cmpt = ComparatorsTool()
    for i in range(testTime):
        arr = cmpt.generateRandomArray(maxSize, maxValue)
        print('############')
        print(arr)
        arr1 = cmpt.copyArray(arr)
        arr2 = cmpt.copyArray(arr)
        res1 = sortLib.mergeSort(arr1)
        res2 = cmpt.comparator(arr2)
        print('res', res1, res2)
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

