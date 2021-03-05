class Solution(object):
    def countBits(self, num):
        res = []
        for i in range(num+1):
            res.append(self.countOnes(i))
        return res

    def countOnes(self, sub_num):
        resOnes = 0
        while sub_num:
            sub_num = sub_num & (sub_num-1)
            resOnes += 1
        return resOnes

if __name__ == '__main__':
    num = 0
    print(Solution().countBits(num))