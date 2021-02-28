class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = []
        self.sub_decodes(s, '', res)
        return len(res)

    def sub_decodes(self, s, sub_str, res):
        decode_dict = {
            1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
            11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V',
            23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
        }
        if len(s) == 0:
            print(sub_str)
            if len(sub_str) > 0:
                res.append(sub_str)
            return res

        flag = 0
        if (len(s) == 1 and int(s[0]) >= 1 and int(s[0]) <= 9) or \
                (len(s) >= 2 and int(s[0]) >= 1 and int(s[0]) <= 9 and int(s[1]) >= 1 and int(s[1]) <= 9):
            new_sub_str = sub_str + decode_dict[int(s[0])]
            self.sub_decodes(s[1:], new_sub_str, res)
            flag = 1


        if len(s) >= 2 and int(s[:2]) >= 10 and int(s[:2]) <= 26:
            new_sub_str = sub_str + decode_dict[int(s[:2])]
            self.sub_decodes(s[2:], new_sub_str, res)
            flag = 1

        if flag == 0:
            res = []
            return []

    def dp_step1(self, s):
        if len(s) < 1:
            return 0
        ch = s[0]
        if int(ch) >= 1 and int(ch) <= 9:
            return 1
        else:
            return 0

    def dp_step2(self, s):
        if len(s) < 2:
            return 0
        ch = s[:2]
        if int(ch) >= 10 and int(ch) <= 26:
            return 1
        else:
            return 0

    def dp_decode(self, s):
        dp = [0 for i in range(len(s))]
        if len(s) == 0 or int(s[0]) == 0:
            return 0
        dp[0] = self.dp_step1(s[0:])
        if len(s) >= 2:
            dp[1] = self.dp_step2(s[0:]) + dp[0] * self.dp_step1(s[1:])
            for i in range(2, len(s)):
                dp[i] = dp[i - 1] * self.dp_step1(s[i:]) + dp[i - 2] * self.dp_step2(s[i - 1:])
        return dp[-1]

if __name__ == '__main__':
    s = "101011111111111111111111111111"
    #print(Solution().numDecodings(s))
    print(Solution().dp_decode(s))