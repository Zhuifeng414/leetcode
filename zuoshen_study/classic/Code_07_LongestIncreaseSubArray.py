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
    arr = [4, 3, 5, 3]
    dp = Solutionn().dps(arr)
    print(dp)
    res = Solutionn().generateLIS(arr, dp)
    print(res[::-1])
    print('===========================>')
    dp = Solutionn().dps_fast(arr)
    print(dp)
    res = Solutionn().generateLIS(arr, dp)
    print(res[::-1])