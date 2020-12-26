class Solution(object):
    def __init__(self):
        return

    def dps(self, arr, aim):
        max_len = 0
        map_dict = {0:-1}
        cum_sum = 0
        for i in range(len(arr)):
            cum_sum += arr[i]
            if cum_sum - aim in map_dict.keys():
                max_len = max(max_len, i - map_dict[cum_sum - aim])
            if cum_sum not in map_dict.keys():
                map_dict[cum_sum] = i
        return max_len


if __name__ == '__main__':
    arr = [1, 2, 3, 3]
    aim = 6
    res = Solution().dps(arr, aim)
    print(res)