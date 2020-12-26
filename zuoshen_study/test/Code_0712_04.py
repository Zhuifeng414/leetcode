class Solution(object):
    def get_dis(self, xs, ys, positions):
        from math import sqrt
        n = len(positions)
        loss = 0
        for i in range(n):
            [xi, yi] = positions[i]
            loss += sqrt((xs - xi) ** 2 + (ys - yi) ** 2)
        return loss

    def getMinDistSum(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: float
        """
        from math import sqrt
        lr = 100
        x_sum = 0
        y_sum = 0
        n = len(positions)
        for item in positions:
            x_sum += item[0]
            y_sum += item[1]
        xs = x_sum/n
        ys = y_sum/n
        loss = self.get_dis(xs, ys, positions)
        delta = 10
        print('init', loss)
        while lr > 1e-8 and delta > 1e-7:
            center = [[max(xs-lr, 0), ys], [min(xs+lr, 100), ys], [xs, max(ys-lr, 0)], [xs, min(ys+lr, 100)]]
            dis_list = [0, 0, 0, 0]
            for i in range(len(center)):
                dis_list[i] = self.get_dis(center[i][0], center[i][1], positions)
            min_dis = min(dis_list)
            index = dis_list.index(min_dis)
            if min_dis > loss:
                lr = lr * 0.5
                print('lr', lr, 'min_dis', min_dis, 'center',  center)
            else:
                [xs, ys] = center[index]
                delta = abs(loss - min_dis)
                loss = min_dis
                print(loss)
        return loss

positions = [[1,1],[0,0],[2,0]]
res = Solution().getMinDistSum(positions)
print(res)
