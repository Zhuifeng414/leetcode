# 作者：fuxuemingzhu
# 链接：https://leetcode-cn.com/problems/next-greater-element-ii/solution/dong-hua-jiang-jie-dan-diao-zhan-by-fuxu-4z2g/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution(object):
    def nextGreaterElements_ans(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        res = [-1] * N
        stack = []
        for i in range(N * 2):
            while stack and nums[stack[-1]] < nums[i % N]:
                print('###', 'stack:', stack, 'res:', res, 'nums:', nums)
                res[stack.pop()] = nums[i % N]
            print('***', 'stack:', stack, 'res:', res, 'nums:', nums)
            stack.append(i % N)
        return res

    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2*n):
            while stack and nums[stack[-1]] < nums[i % n]:
                res[stack.pop()] = nums[i % n]
            stack.append(i % n)
        return res




if __name__ == '__main__':
    nums = [5, 4, 3, 2, 1]
    print(Solution().nextGreaterElements(nums))
