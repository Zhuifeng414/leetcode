class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return

    def process(self, flag0, flag_index, index, sub_sum, nums):
        if index > len(nums) - 1:
            return sub_sum

        if flag_index == 1:
            self.process(flag0, 0, index + 1, sub_sum, nums)
            return sub_sum

        elif flag_index == 0:
            if (flag0 == 1) and (index + 1 == len(nums)-1):
                self.process(flag0, 1, index + 1, sub_sum, nums)
            else:
                self.process(flag0, 1, index + 1, sub_sum + nums[index], nums)
            self.process(flag0, 0, index + 1, sub_sum, nums)

if __name__ == '__main__':
    print('hello world !')