class StringCross:
    def __init__(self):
        return

    def isCross1(self, s1, s2, ai):
        if len(s1) == 0 or len(s2) == 0 or len(ai) == 0:
            return False
        str1 = s1
        str2 = s2
        aim = ai
        if len(aim) != len(str1) + len(str2):
            return False

        dp = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
        dp[0][0] = True
        for i in range(1, len(str1)):
            if str1[i - 1] != aim[i - 1]:
                break
            dp[i][0] = True

        for j in range(1, len(str2)):
            if str2[j - 1] != aim[j - 1]:
                break
            dp[0][j] = True

        for i in range(1, len(str1)+1):
            for j in range(1, len(str2)+1):
                # str1 的最后一个字符和aim的最后一个字符相等时，
                # 只要str1 的前 i-1 个字符 + str2的前j个字符可以
                # 交错出aim的 i+j-1 个字符即可
                ## 或者
                # str2 的最后一个字符和aim的最后一个字符相等时，
                # 只要str2 的前 j-1 个字符 + str1的前i个字符可以
                # 交错出aim的 i+j-1 个字符即可
                if (str1[i - 1] == aim[i + j - 1] and dp[i - 1][j])\
                        or (str2[j - 1] == aim[i + j - 1] and dp[i][j - 1]):
                    dp[i][j] = True
        return dp[len(str1)][len(str2)]

if __name__ == '__main__':
    str1 = '1234'
    str2 = 'abcd'
    aim = '1a2b3c4d'
    print(StringCross().isCross1(str1, str2, aim))

