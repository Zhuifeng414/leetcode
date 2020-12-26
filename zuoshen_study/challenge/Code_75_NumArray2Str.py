class Solution(object):
    def __init__(self):
        return

    def num2str(self, num_str):
        if num_str in num2str.keys():
            return num2str[num_str]
        else:
            return -1

    def process(self, arr, index, res_str):
        if index >= len(arr):
            print(res_str)
            return 1
        if self.num2str(arr[index]) == -1:
            p1 = 0
        else:
            p1_res_str = res_str + self.num2str(arr[index])
            p1 = self.process(arr, index+1, p1_res_str)

        if self.num2str(arr[index:index+2]) == -1 or index+1 >= len(arr):
            p2 = 0
        else:
            p2_res_str = res_str + self.num2str(arr[index:index+2])
            p2 = self.process(arr, index + 2, p2_res_str)
        return p1 + p2

    def dps(self, arr):
        if len(arr) == 0:
            return 0
        dp = [0 for i in range(len(arr)+1)]
        dp[0] = 0
        dp[1] = 1 if (self.num2str(arr[0]) != -1) else 0
        p1 = dp[1] if (self.num2str(arr[2]) != -1 and dp[1] > 0) else 0
        p2 = 1 if (self.num2str(arr[:2]) != -1) else 0
        dp[2] = p1 + p2
        print(dp)
        for i in range(3, len(arr)+1):
            p1 = dp[i-1] if (self.num2str(arr[i-1]) != -1 and dp[i-1] > 0) else 0
            p2 = dp[i-2] if (self.num2str(arr[i-2:i]) != -1 and dp[i-2] > 0) else 0
            dp[i] = p1 + p2
        print(dp)
        return dp

if __name__ == '__main__':
    num2str = {
        '1':'A', '2':'B', '3':'C', '4':'D', '5':'E', '6':'F',
        '7':'G', '8':'H', '9':'I', '10':'J', '11':'K', '12':'L',
        '13':'M', '14':'N', '15':'O', '16':'P', '17':'Q', '18':'R',
        '19':'S', '20':'T', '21':'U', '22':'V', '23':'W', '24':'X', '25':'Y', '26':'Z'
    }

    num_arr = '1111'
    print(Solution().process(num_arr, 0, ''))
    print('>>>==============>>>')
    dp = Solution().dps(num_arr)