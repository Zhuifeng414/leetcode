class Solution(object):
    def process(self, arr, di, dj, bsum, res):
        if di >= len(arr):
            res.append(bsum)
            return bsum
        r = []
        p = []
        for j in range(len(arr[di])):
            if j != dj:
                r.append(arr[di][j])
                p.append(j)
        #print(r, p)
        min_r = min(r)
        min_p = p[r.index(min_r)]
        self.process(arr, di+1, min_p, bsum+min_r, res)



    def minFallingPathSum(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """
        if len(arr) == 0 or len(arr[0]) == 0:
            return 0
        bsum = 0
        res = []
        self.process(arr, 0, -1, bsum, res)
        return min(res)

arr = [[1,2,3],[4,5,6],[7,8,9]]
res = Solution().minFallingPathSum(arr)
print(res)


# 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
#
# 你需要按照以下要求，帮助老师给这些孩子分发糖果：
#
# 每个孩子至少分配到 1 个糖果。
# 相邻的孩子中，评分高的孩子必须获得更多的糖果。
# 那么这样下来，老师至少需要准备多少颗糖果呢？
#
# 示例 1:
#
# 输入: [1,0,2]
# 输出: 5
# 解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
# 示例 2:
#
# 输入: [1,2,2]
# 输出: 4
# 解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
#      第三个孩子只得到 1 颗糖果，这已满足上述两个条件。