# 给出由小写字母组成的字符串S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
# 在S上反复执行重复项删除操作，直到无法继续删除。
# 在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
# 示例：
#
# 输入："abbaca"
# 输出："ca"
# 解释：
# 例如，在
# "abbaca"
# 中，我们可以删除
# "bb"
# 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串
# "aaca"，其中又只有
# "aa"
# 可以执行重复项删除操作，所以最后的字符串为
# "ca"。
#
#
# 提示：
#
# 1 <= S.length <= 20000
# S
# 仅由小写英文字母组成。
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        if len(S) <= 1:
            return S
        L = 0
        R = 1
        tmp =0
        delete_index = []
        while R < len(S):
            if S[L] != S[R]:
                L = R
                R += 1
                tmp += 1
            else:
                delete_index.append(L)
                delete_index.append(R)
                if tmp == 0:
                    L = R+1
                    R += 2
                else:
                    tmp -= 1
                    L -= 1
                    while L in delete_index:
                        L -= 1
                    R += 1
        res = ''
        for i in range(len(S)):
            if i not in delete_index:
                res += S[i]
        return res
# "ibfjcaccadid"
# "ibfjcaadidiaidchakchchcahabhibdcejkdkfbecdjhajbkfebebfea"
# "ibfjcdidi  aidchakchchcahabhibdcejkdkfbecdjhajbkfebebfea"  --
if __name__ == '__main__':
    S = '"ibfjcaffccadidiaidchakchchcahabhibdcejkdkfbaeeaecdjhajbkfebebfea"'
    res = Solution().removeDuplicates(S)
    print(res)



