class Info(object):
    def __init__(self, w=0, h=0):
        self.w = w
        self.h = h

import functools
def cmp(a, b):
    # 从 小 到 大
    if a.h > b.h:
        return 1
    if a.h < b.h:
        return -1
    if a.h == b.h:
        # 从 大 到 小
        if a.w > b.w:
            return -1
        if a.w < b.w:
            return 1
    return 0

class Solutionn(object):
    def __init__(self):
        return

    def dps(self, arr):
        dp = [0 for i in range(len(arr))]
        dp[0] = 1
        for i in range(1, len(arr)):
            dp_sub_max = 0
            for j in range(i):
                if arr[j] < arr[i]:
                    dp_sub_max = max(dp_sub_max, dp[j])
            dp[i] = dp_sub_max + 1
        return dp

    def dps_fast(self, arr):
        dp = [0 for i in range(len(arr))]
        ends = [0 for i in range(len(arr))]
        right = 0
        dp[0] = 1
        ends[0] = arr[0]
        for i in range(1, len(arr)):
            l = 0
            r = right
            while l <= r:
                mid = int((l + r) / 2)
                if ends[mid] < arr[i]:
                    l = mid+1
                else:
                    r = mid-1
            right = max(right, l)
            # 所有长度为l+1的递增序列中，最小结尾数是arr[i]
            # 这里一定可以替换吗？ yes
            ends[l] = arr[i]
            dp[i] = l + 1
        return dp


    def generateLIS(self, arr, dp):
        max_dp = dp[0]
        max_index = 0
        res = []
        for i in range(len(dp)):
            if dp[i] >= max_dp:
                max_index = i
                max_dp = dp[i]
        index_value = arr[max_index]
        res.append(index_value)
        for i in range(max_index-1, -1, -1):
            if arr[i] < index_value and dp[i] == max_dp - 1:
                index_value = arr[i]
                max_dp = dp[i]
                res.append(index_value)
        return res

if __name__ == '__main__':
    # Info: w h
    # h 从小到大 w 从大到小
    arr = [Info(3, 4), Info(2, 6), Info(5, 6), Info(1, 5), Info(7, 5)]
    res = sorted(arr, key=functools.cmp_to_key(cmp))
    w_arr = [0 for i in range(len(arr))]
    for i in range(len(res)):
        item = res[i]
        print(item.w, item.h)
        w_arr[i] = item.w
    ######################################
    dp = Solutionn().dps_fast(w_arr)
    print(dp)
    res = Solutionn().generateLIS(w_arr, dp)
    print(res[::-1])


