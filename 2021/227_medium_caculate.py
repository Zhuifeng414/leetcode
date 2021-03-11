# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
#
# 整数除法仅保留整数部分。
#
# 输入：s = "3+2*2"
# 输出：7
###########################################################
# class Solution {
# public int calculate(String s) {
# Deque < Integer > stack = new LinkedList < Integer > ();
# char preSign = '+';
# int num = 0;
# int n = s.length();
# for (int i = 0; i < n; ++i) {
# if (Character.isDigit(s.charAt(i))) {
# num = num * 10 + s.charAt(i) - '0';
# }
# if (!Character.isDigit(s.charAt(i)) & & s.charAt(i) != ' ' | | i == n - 1) {
# switch (preSign) {
# case '+':
#     stack.push(num);
#
#
#     break;
# case
# '-':
# stack.push(-num);
# break;
# case
# '*':
# stack.push(stack.pop() * num);
# break;
# default:
# stack.push(stack.pop() / num);
# }
# preSign = s.charAt(i);
# num = 0;
# }
# }
# int
# ans = 0;
# while (!stack.isEmpty()) {
# ans += stack.pop();
# }
# return ans;
# }
# }


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stk = []
        pre_sign = '+'
        num = 0
        res = 0
        for i in range(len(s)):
            if s[i] >= '0' and s[i] <= '9':
                num = num*10 + ord(s[i]) - ord('0')
            if  (not(s[i] >= '0' and s[i] <= '9') and s[i] != ' ') or i == len(s)-1:
                if pre_sign == '+':
                    stk.append(num)
                elif pre_sign == '-':
                    stk.append(0-num)
                elif pre_sign == '*':
                    stk.append(int(stk.pop() * num))
                elif pre_sign == '/':
                    stk.append(int(stk.pop()*1.0 / num))
                num = 0
                pre_sign = s[i]
        res = sum(stk)
        return res

if __name__ == '__main__':
    s = "14-3/2"
    print(Solution().calculate(s))