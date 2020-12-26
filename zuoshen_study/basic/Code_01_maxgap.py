import random
# 数组的小和问题
class MaxGap:

    def __init__(self):
        # do nothing
        return

    def bucket(self, num, len_nums, min_value, max_value):
        return int((num - min_value) * len_nums / (max_value - min_value))

    def maxGap(self, nums):
        if len(nums) < 2:
            return 0

        len_nums = len(nums)
        min_value = nums[0]
        max_value = nums[0]
        for i in range(len_nums):
            min_value = min(min_value, nums[i])
            max_value = max(max_value, nums[i])
        if min_value == maxValue:
            return 0

        maxs = [0] * (len_nums + 1)
        mins = [0] * (len_nums + 1)
        hasNum = [0] * (len_nums + 1)
        bid = 0
        for i in range(len_nums):
            bid = self.bucket(nums[i], len_nums, min_value, max_value)
            mins[bid] = min(mins[bid], nums[i]) if hasNum[bid] == 1 else nums[i]
            maxs[bid] = max(maxs[bid], nums[i]) if hasNum[bid] == 1 else nums[i]
            hasNum[bid] = 1

        res = 0
        lastMax = maxs[0]
        lastMin = mins[0]
        for i in range(1, len_nums+1):
            if hasNum[i]:
                res = max(res, mins[i] - lastMax)
                #res = max(res, maxs[i] - lastMin)
                lastMax = maxs[i]
                #lastMin = mins[i]
        return res


class ComparatorsTool:
    def __init__(self):
        # do nothing
        return

    # 一种简单 好实现的准确方法
    def comparator(self, arr):
        if len(arr) < 2:
            return 0
        arr.sort()
        res = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            res = max(res, arr[i+1] - arr[i])
        return res

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
    sortLib = MaxGap()
    cmpt = ComparatorsTool()
    for i in range(testTime):
        arr = cmpt.generateRandomArray(maxSize, maxValue)
        print('############')
        print(arr)
        arr1 = cmpt.copyArray(arr)
        arr2 = cmpt.copyArray(arr)
        res1 = sortLib.maxGap(arr1)
        res2 = cmpt.comparator(arr2)
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

