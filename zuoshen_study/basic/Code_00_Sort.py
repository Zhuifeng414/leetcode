import random

class MySortLib:

    def __init__(self):
        # do nothing
        return

    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

    # 冒泡排序 O(n^2)
    def bubbleSort(self, arr):
        if len(arr) < 2:
            return
        for i in range(len(arr)):
            for j in range(0, len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    self.swap(arr, j, j+1)
        return

    # 插入排序 O(n^2)
    def insertionSort(self, arr):
        if len(arr) < 2:
            return
        for i in range(1, len(arr)):
            for j in range(i-1, -1, -1):
                #print(arr, i, j)
                if arr[j+1] < arr[j]:
                    self.swap(arr, j+1, j)
        return

    # 选择排序 O(n^2)
    def selectionSort(self, arr):
        if len(arr) < 2:
            return
        for i in range(len(arr)-1):
            minIndex = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[minIndex]:
                    minIndex = j
            self.swap(arr, i, minIndex)
        return

    # 归并排序
    def mergeSort(self, arr):
        if len(arr) < 2:
            return
        self.merge_sort(arr, 0, len(arr)-1)

    def merge_sort(self, arr, l, r):
        if l == r:
            return
        mid = (l + r)//2
        #print('merge_sort', arr, l, mid, r)
        self.merge_sort(arr, l, mid)
        self.merge_sort(arr, mid+1, r)
        self.merge(arr, l, mid, r)
        return

    def merge(self, arr, l, m, r):
        help = [0]*(r - l + 1)
        i = 0
        p1 = l
        p2 = m + 1
        while p1 <= m and p2 <= r:
            if arr[p1] < arr[p2]:
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
        return


    def bucketSort(self, arr):
        if len(arr) < 2:
            return
        max_value = arr[0]
        for i in range(1, len(arr)):
            max_value = max(max_value, arr[i])
        bucket = [0]*(max_value + 1)
        for i in range(len(arr)):
            bucket[arr[i]] += 1
        index = 0
        for i in range(len(bucket)):
            for j in range(bucket[i]):
                arr[index] = i
                index += 1


#####################################
## 堆排序
class HeapSort:
    def __init__(self):
        # do nothing
        return

    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

    def heapInsert(self, arr, index):
        while arr[index] > arr[int((index-1)/2)]:
            self.swap(arr, index, int((index-1)/2))
            index = int((index-1)/2)

    def heapify(self, arr, index, size):
        left = index*2 + 1
        right = left + 1
        while(left < size):
            largest = right if right < size and arr[right] > arr[left] else left
            largest = largest if arr[largest] > arr[index] else index
            if largest == index:
                break #父节点已经是最大
            self.swap(arr, largest, index) #父节点下沉到最大的孩子中, 将最大值换到父节点
            index = largest
            left = index * 2 + 1 #新的左孩子

    def heapSort(self, arr):
        if len(arr) < 2:
            return
        for i in range(len(arr)):
            self.heapInsert(arr, i)
        size = len(arr) - 1
        self.swap(arr, 0, size)
        while size > 0:
            self.heapify(arr, 0, size)
            size -= 1
            self.swap(arr, 0, size)
            print('here:', arr)


## 随机快排
class QuickSort:
    def __init__(self):
        # do nothing
        return

    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

    def partition(self, arr, l, r):
        less = l - 1
        more = r
        cur = l
        while cur < more:
            if arr[cur] < arr[r]:
                less += 1
                self.swap(arr, less, cur) #小于区域的和等于区域的交换
                cur += 1
            elif arr[cur] > arr[r]:
                more -= 1
                self.swap(arr, cur, more) # 大于区域的和最右侧的交换，继续考察右侧交换过来的元素
            else:
                cur += 1
        self.swap(arr, more, r)
        return [less+1, more] #边界

    def quick_sort_sub(self, arr, l, r):
        if l < r:
            self.swap(arr, l+int(random.random()*(r-l)), r) #随机快排
            p = self.partition(arr, l, r)
            self.quick_sort_sub(arr, l, p[0]-1) #最左侧小于主元的index为p[0]-1
            self.quick_sort_sub(arr, p[1]+1, r) #最右侧大于主元的index为p[1]+1

    def quickSort(self, arr):
        if len(arr) < 2:
            return arr
        self.quick_sort_sub(arr, 0, len(arr)-1)

####################################
class ComparatorsTool:
    def __init__(self):
        # do nothing
        return

    # 一种简单 好实现的准确方法
    def comparator(self, arr):
        return arr.sort()

    # 随机list生成器
    def generateRandomArray(self, maxSize, maxValue):
        arr = []
        size = int(random.random()*(maxSize+1))
        for i in range(size):
            #value = int(random.random()*(maxValue+1)) - int(random.random()*(maxValue))
            value = int(random.random() * (maxValue + 1)) #非负数
            arr.append(value)
        return arr

    # 复制Array
    def copyArray(self, arr):
        res = [item for item in arr]
        return res

    # 比较两个Array是否相等
    def isEqual(self, arr1, arr2):
        if len(arr1) != len(arr2):
            return False
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False
        return True

    def printArray(self, arr):
        for item in arr:
            print(item, ' ')


if __name__ == '__main__':
    testTime = 50
    maxSize = 10
    maxValue = 10
    succeed = True
    sortLib = MySortLib()
    cmpt = ComparatorsTool()
    for i in range(testTime):
        arr = cmpt.generateRandomArray(maxSize, maxValue)
        arr1 = cmpt.copyArray(arr)
        arr2 = cmpt.copyArray(arr)
        sortLib.bucketSort(arr1)
        cmpt.comparator(arr2)
        if not cmpt.isEqual(arr1, arr2):
            succeed = False
            break
    if succeed:
        print('Nice!')
    else:
        print('Fucking fucked!')
        print('arr', arr)
        print('arr1', arr1)
        print('arr2', arr2)

