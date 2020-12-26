import sys
class Solution(object):
    def __init__(self):
        return

    def print_dp(self, dp):
        for item in dp:
            print(item)

    def dps(self, str1, str2):
        dp = [[0 for i in range(len(str2))] for j in range(len(str1))]
        max_res = 0
        sub1 = str1[0]
        for i in range(len(str2)):
            sub2 = str2[i]
            if sub1 == sub2:
                dp[0][i] = 1
                max_res = 1

        sub2 = str2[0]
        for i in range(len(str1)):
            sub1 = str1[i]
            if sub1 == sub2:
                dp[0][i] = 1
                max_res = 1

        for i in range(1, len(str1)):
            for j in range(1, len(str2)):
                dp[i][j] = (dp[i-1][j-1] + 1) if str1[i] == str2[j] else 0
                max_res = max(max_res, dp[i][j])
        #self.print_dp(dp)
        return max_res

    def dps_zip(self, str1, str2):
        if len(str1) == 0 or len(str2) == 0:
            return ''

        all_res = ''
        max_res = 0
        for i in range(len(str2)-1, -1, -1):
            delta = len(str2) - i
            sub_res = ''
            tmp = 0
            for j in range(min(delta, len(str1))):
                if str2[i+j] == str1[j]:
                    sub_res += str1[j]
                    tmp = tmp + 1
                    if tmp > max_res:
                        max_res = tmp
                        all_res = sub_res
                else:
                    tmp = 0
                    sub_res = ''

        if max_res >= min(len(str1), len(str2)):
            return all_res
        else:
            for i in range(1, len(str1)):
                delta = len(str1) - i
                sub_res = ''
                tmp = 0
                for j in range(min(delta, len(str2))):
                    if str1[i+j] == str2[j]:
                        sub_res += str2[j]
                        tmp = tmp + 1
                        if tmp > max_res:
                            max_res = tmp
                            all_res = sub_res
                    else:
                        tmp = 0
                        sub_res = ''
        #print(all_res)
        return all_res

    def dps_new(self, str1, str2):
        if len(str1) == 0 or len(str2) == 0:
            return ''
        row = 0
        col = len(str2)-1
        max_res = 0
        end = 0
        while row < len(str1):
            i = row
            j = col
            tmp = 0
            while i < len(str1) and j < len(str2):
                if str1[i] != str2[j]:
                    tmp = 0
                else:
                    tmp += 1
                if tmp > max_res:
                    max_res = tmp
                    end = i
                i += 1
                j += 1

            if col > 0:
                col -= 1
            else:
                row += 1
        return str1[end-max_res+1: end+1]

if __name__ == '__main__':
    str1 = 'wang432tesla345'
    str2 = 'tesla345wang414'
    # str1 = sys.stdin.readline()
    # str2 = sys.stdin.readline()
    # print(Solution().dps(str1, str2))
    # print('=======================>')
    print(Solution().dps_zip(str1, str2))