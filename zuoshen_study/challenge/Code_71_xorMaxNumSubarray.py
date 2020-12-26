class Solution(object):
    def __init__(self):
        return

    def dps(self, arr):
        if len(arr) == 0:
            return 0
        dp = [0 for i in range(len(arr))]
        xor_sum = arr[0]
        print(0, xor_sum)
        xor_sum_dict = {}
        xor_sum_dict[0] = -1
        xor_sum_dict[xor_sum] = 0
        dp[0] = 1 if xor_sum == 0 else 0
        for i in range(1, len(arr)):
            p1 = dp[i-1]
            p2 = 0
            xor_sum = xor_sum ^ arr[i]
            print(i, xor_sum)
            if xor_sum not in xor_sum_dict.keys():
                xor_sum_dict[xor_sum] = i
            else:
                index = xor_sum_dict[xor_sum]
                p2 = dp[index] + 1
                xor_sum_dict[xor_sum] = i
            dp[i] = max(p1, p2)
        print(dp)
        print(xor_sum_dict)
        return dp

if __name__ == '__main__':
    arr = [0, 6, 3, 2, 1]
    dp = Solution().dps(arr)


