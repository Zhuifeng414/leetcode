import matplotlib.pyplot as plt

class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        from math import sin, cos, pi, sqrt
        from random import uniform
        r = sqrt(uniform(0, self.radius))
        theta = uniform(0, 2 * pi)
        x = r * cos(theta) + self.x_center
        y = r * sin(theta) + self.y_center
        return [x, y]



# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
p = Solution(2, 0, 0)
xlist = []
ylist = []
for i in range(1000):
    [xt, yt] = p.randPoint()
    xlist.append(xt)
    ylist.append(yt)
plt.plot(xlist, ylist, 'b.')
plt.show()
