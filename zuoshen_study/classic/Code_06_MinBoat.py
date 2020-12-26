class Solution(object):
    def __init__(self):
        return

    def minBoat(self, arr, limit):
        if len(arr) == 0:
            return 0
        # 无法完成任务
        if arr[-1] > limit:
            return 0
        lessR = -1
        for i in range(len(arr)-1, -1, -1):
            if arr[i] <= int(limit/2):
                lessR = i
                break
        # 没有小于limit/2的元素
        if lessR == -1:
            return len(arr)
        L = lessR
        R = lessR + 1
        lessUnused = 0
        while L >= 0:
            solved = 0
            while R < len(arr) and arr[L]+arr[R] <= limit:
                R += 1
                solved += 1 #单次配对的数量
            if solved == 0:
                lessUnused += 1 #左侧未配对的数量
                L -= 1
            else:
                L = max(-1, L-solved)

        lessAll = lessR + 1 # 左侧总个数 （ <= limit/2 区域）
        lessUsed = lessAll - lessUnused # 总体配对的数量
        moreUnsolved = len(arr) - lessR - 1 - lessUsed # 右侧没有配对的数量
        # 配对数量 + 左侧未配对/2 + 右侧未配对
        return lessUsed + ((lessUnused+1)>>1) + moreUnsolved

if __name__ == '__main__':
    arr = [1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5]
    limit = 6
    print(Solution().minBoat(arr, limit))