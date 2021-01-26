import collections
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        def str_element(item):
            if item[0] > item[1]:
                return str([item[1], item[0]])
            else:
                return str([item[0], item[1]])

        res_dict = collections.defaultdict()
        for item in dominoes:
            if str_element(item) in res_dict.keys():
                res_dict[str_element(item)] += 1
            else:
                res_dict[str_element(item)] = 1

        res = 0
        for k, v in res_dict.items():
            res += v*(v-1)/2
        return int(res)

if __name__ == '__main__':
    dominoes = [[1, 2], [2, 1], [1, 2], [2, 1]]
    print(Solution().numEquivDominoPairs(dominoes))