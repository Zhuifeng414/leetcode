# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。
# 如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。
# 所谓的朋友圈，是指所有朋友的集合。
#
# 给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，
# 表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。
# 你必须输出所有学生中的已知的朋友圈总数。
#
# 示例 1:
#
# 输入:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# 输出: 2
# 说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回2。
# 示例 2:
#
# 输入:
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# 输出: 1
# 说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
# 注意：
#
# N 在[1,200]的范围内。
# 对于所有学生，有M[i][i] = 1。
# 如果有M[i][j] = 1，则有M[j][i] = 1。
#

class Solution(object):
    def find_one(self, M, index):
        n = len(M)
        delta = int((n - index)/2)
        for i in range(delta, index-1):
            if M[delta][i] == 1:
                return [delta, i]
        for i in range(delta, index-1):
            if M[i][n-delta] == 1:
                return [i, n-delta]
        for i in range(n-delta, delta-1, -1):
            if M[n-delta][i] == 1:
                return [n-delta, i]
        for i in range(n-delta, delta-1, -1):
            if M[i][delta] == 1:
                return [i, delta]

    def print_one(self, M, index):
        n = len(M)
        delta = int((n - index) / 2)
        for i in range(0, index - 1):
            #print(M[delta][delta + i])
            if M[delta][delta + i] == 1:
                return [delta, delta + i]
        for i in range(0, index - 1):
            #print(M[delta + i][n - 1 - delta])
            if M[delta + i][n - 1 - delta] == 1:
                return [delta + i, n - 1 - delta]
        for i in range(0, index - 1):
            #print(M[n - 1 - delta][n - 1 - delta - i])
            if M[n - 1 - delta][n - 1 - delta - i] == 1:
                return [n - 1 - delta, n - 1 - delta - i]
        for i in range(0, index - 1):
            #print(M[n - 1 - delta - i][delta])
            if M[n - 1 - delta - i][delta] == 1:
                return [n - 1 - delta - i, delta]
        return [-1, -1]

    def search_map(self, M, x0, y0, index):
        n = len(M)
        delta = int((n - index) / 2)
        L = delta
        R = n - 1 - delta
        U = delta
        D = n - 1 - delta
        stack = [[x0, y0]]

        while len(stack) > 0:
            [x, y] = stack.pop(0)
            # up
            if U <= x - 1 <= D and L <= y <= R and M[x-1][y] == 1:
                stack.append([x-1, y])

            # down
            if U <= x + 1 <= D and L <= y <= R and M[x+1][y] == 1:
                stack.append([x+1, y])

            # left
            if U <= x <= D and L <= y - 1 <= R and M[x][y-1] == 1:
                stack.append([x, y-1])

            # right
            if U <= x <= D and L <= y + 1 <= R and M[x][y+1] == 1:
                stack.append([x, y+1])

            M[x][y] = 0
        return


    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        index = n
        count = 0
        while index >= 2:
            [x0, y0] = self.print_one(M, index)
            if x0 != -1:
                count += 1
                self.search_map(M, x0, y0, index)
            else:
                index = index - 2
        if index == 1:
            delta = int((n - index) / 2)
            if M[delta][delta] == 1:
                count += 1
        return count

if __name__ == '__main__':
    M = \
    [[1,0,0,1],
     [0,1,1,0],
     [0,1,1,1],
     [1,0,1,1]]
    res = Solution().findCircleNum(M)
    print(res)
