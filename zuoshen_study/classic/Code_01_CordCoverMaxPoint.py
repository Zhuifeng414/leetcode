import random
class CordCoverMaxPoint:
    def __init__(self):
        return

    #求解大于value的最左侧的index
    def nearestIndex(self, arr, R, value):
        L = 0
        index = R #没有符合条件的就返回右边界本身
        while L <= R:
            mid = int((L + R)/2)
            if arr[mid] >= value:
                index = mid
                R = mid - 1
            else:
                L = mid + 1
        return index

    def maxPoint1(self, arr, length):
        res = 1
        for i in range(0, len(arr)):
            nearest = self.nearestIndex(arr, i, arr[i] - length)
            res = max(res, i - nearest + 1)
            #print(i, res)
        return res

    def maxPoint2(self, arr, length):
        left = 0
        right = 0
        res = 1
        N = len(arr)
        while left < N:
            while right < N and arr[right] - arr[left] <= length:
                right += 1
            res = max(res, right - left) # 这里的right已经越界了，所以不再是right-left+1
            left += 1
        return res

class ComparatorsTool:
    def __init__(self):
        # do nothing
        return

    # 一种简单 好实现的准确方法
    def comparator(self, arr, length):
        res = 0
        for i in range(0, len(arr)):
            pre = i - 1
            while pre >= 0 and arr[i] - arr[pre] <= length:
                pre -= 1
            res = max(res, i - pre)
        return res

    # 随机list生成器
    def generateRandomArray(self, maxSize, maxValue):
        arr = []
        size = max(int(random.random()*(maxSize+1)), 1)
        for i in range(size):
            #value = int(random.random()*(maxValue+1)) - int(random.random()*(maxValue))
            value = int(random.random() * (maxValue + 1))
            arr.append(value)
        arr.sort()
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
    maxSize = 10
    maxValue = 12
    times = 10
    status = True
    for i in range(times):
        arr = ComparatorsTool().generateRandomArray(maxSize, maxValue)
        length = int(random.random() * (maxValue + 1))
        res1 = CordCoverMaxPoint().maxPoint1(arr, length)
        res2 = CordCoverMaxPoint().maxPoint2(arr, length)
        res3 = ComparatorsTool().comparator(arr, length)
        if res1 != res2 or res2 != res3 or res1 != res3:
            status = False
            break
    if status:
        print('Nice !')
    else:
        print('Ooops ~', arr)

