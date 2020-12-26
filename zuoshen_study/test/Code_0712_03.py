class Solution(object):

    def getMinDistSum(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: float
        """
        from math import sqrt
        lr = 1
        x_sum = 0
        y_sum = 0
        n = len(positions)
        for item in positions:
            x_sum += item[0]
            y_sum += item[1]
        xs = x_sum/n
        ys = y_sum/n

        dis_sum = 1e6
        delta = 10
        while delta > 1e-7:
            dis = [0 for i in range(n)]
            dx = [0 for i in range(n)]
            dy = [0 for i in range(n)]
            loss = 0
            dx_sum = 0
            dy_sum = 0
            for i in range(n):
                [xi, yi] = positions[i]
                dis[i] = sqrt((xs - xi) ** 2 + (ys - yi) ** 2)

                if dis[i] == 0:
                    dx[i] = 0
                    dy[i] = 0
                else:
                    dx[i] = (xs - xi) / dis[i]
                    dy[i] = (ys - yi) / dis[i]

                dx_sum += dx[i]
                dy_sum += dy[i]

                loss += dis[i]

            xs = xs - lr * loss * dx_sum
            ys = ys - lr * loss * dy_sum
            delta = abs(loss - dis_sum)
            if loss > dis_sum:
                lr = 0.5*lr
            dis_sum = loss
        return loss
