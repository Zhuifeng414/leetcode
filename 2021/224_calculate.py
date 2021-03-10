class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ops = [1]
        sign = 1
        res = 0
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = ops[-1]
                i += 1
            elif s[i] == '-':
                sign = -1 * ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                while s[i] >= '0' and s[i] <= '9':
                    num = num * 10  + ord(s[i]) - ord('0')
                    i += 1
                res += sign * num
        return res

if __name__ == '__main__':
    s = "(1+(4+5+2)-3)+(6+8)"
    print(Solution().calculate(s))



