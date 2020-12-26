class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1 if s[0] == '1' else 0
        L = -1
        R = 0
        bc = {}
        tmp = 0
        while R < len(s):
            if s[R] == '1':
                if tmp == 1:
                    R += 1
                else:
                    tmp = 1
                    L = R
                    R = R + 1
            else:
                if tmp == 1:
                    tmp = 0
                    if (R - L) in bc.keys():
                        bc[R - L] += 1
                    else:
                        bc[R - L] = 1
                else:
                    R = R + 1
        if tmp == 1:
            if (R - L) in bc.keys():
                bc[R - L] += 1
            else:
                bc[R - L] = 1
        res = 0
        for item in bc.keys():
            res += (bc[item] * item * (item + 1) >> 1) % (1e9 + 7)
        return int(res % (1e9 + 7))

s = "1111111111011010011"
res = Solution().numSub(s)
print(res)



