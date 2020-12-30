# 仅仅反转字母
# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
#  示例 ：
# 输入："Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!" 仅仅反转字母
# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
#  示例 ：
# 输入："Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
class reverse(object):

    def __init__(self):
        return

    def reverse_string(self, init_str):
        init_str = [item for item in init_str]
        str_content = [item for item in init_str if self.is_char(item)][::-1]
        #print(init_str, str_content)
        j = 0
        for i in range(len(init_str)):
            if self.is_char(init_str[i]):
                init_str[i] = str_content[j]
                j += 1
        return ''.join(init_str)

    def fast_reverse_string(self, init_str):
        init_str = [item for item in init_str]
        if len(init_str) <= 1:
            return ''.join(init_str)
        p, q = 0, len(init_str) - 1
        while p < q:
            while (not self.is_char(init_str[p])) and (p < q):
                p += 1
            while (not self.is_char(init_str[q])) and (p < q):
                q -= 1
            if p < q:
                init_str[p], init_str[q] = init_str[q], init_str[p]
                p += 1
                q -= 1
        return ''.join(init_str)

    def is_char(self, tst):
        if (tst >= 'a' and tst <= 'z') or (tst >= 'A' and tst <= 'Z'):
            return True
        else:
            return False

if __name__ == '__main__':
    print('tst')
    # init_str = 'Test1ng-Leet=code-Q!'
    # ans = 'Qedo1ct-eeLg=ntse-T!'
    check_list = [
        ['Test1ng-Leet=code-Q!', 'Qedo1ct-eeLg=ntse-T!'],
        ['123', '123'],
        ['1', '1'],
        ['', ''],
        ['a', 'a'],
        ['aB', 'Ba'],
        ['a1b', 'b1a'],
        ['a23b', 'b23a']
    ]

    for [init_str, ans] in  check_list:
        #res = reverse().reverse_string(init_str)
        res = reverse().fast_reverse_string(init_str)
        if ans == res:
            print('yes:', init_str)
        else:
            print('error!', '\ninit_str:', init_str, '\nans:', ans, '\nyours:', res)


