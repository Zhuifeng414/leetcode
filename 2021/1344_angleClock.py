class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        angle_hour = 30 * (hour + minutes/60.0)
        angle_miutes = 360 / (12 * 5) * minutes
        #print(angle_hour, angle_miutes)
        if abs(angle_hour - angle_miutes)  <= 180:
            return abs(angle_hour - angle_miutes)
        else:
            return 360 - abs(angle_hour - angle_miutes)
if __name__ == '__main__':
    hour = 12
    minutes = 30
    print(Solution().angleClock(hour, minutes))