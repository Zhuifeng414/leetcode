class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        freq_dict = {}
        max_freq = 0
        for row in wall:
            sub_res = 0
            for item in row[:-1]:
                sub_res += item
                if sub_res in freq_dict.keys():
                    freq_dict[sub_res] += 1
                else:
                    freq_dict[sub_res] = 1
                print('now', max_freq, freq_dict[sub_res])
                if max_freq < freq_dict[sub_res]:
                    max_freq = freq_dict[sub_res]
        print(freq_dict)
        return len(wall) - max_freq

if __name__ == '__main__':
    wall = [[7, 1, 2], [3, 5, 1, 1], [10]]
    print(Solution().leastBricks(wall))