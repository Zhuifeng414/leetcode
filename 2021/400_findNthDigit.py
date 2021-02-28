class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """

        sf = 9
        pre_sf = 0
        bit_num = 1
        while sf < n and 10 ** bit_num < 2 ** 31:
            bit_num += 1
            pre_sf = sf
            sf += bit_num * 10 ** (bit_num - 1) * 9
        last_num = (n - pre_sf - 1) // bit_num + 10 ** (bit_num - 1)
        res = str(last_num)[((n - pre_sf) % bit_num) - 1]
        return res

