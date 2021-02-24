class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        ch_dict = {}
        for item in A[0]:
            if item in ch_dict.keys():
                ch_dict[item] += 1
            else:
                ch_dict[item] = 1

        for sub_str in A[1:]:
            sub_dict = {}
            for item in sub_str:
                if item in sub_dict.keys():
                    sub_dict[item] += 1
                else:
                    sub_dict[item] = 1

            for k, v in ch_dict.items():
                if k in sub_dict.keys():
                    ch_dict[k] = min(sub_dict[k], v)
                else:
                    ch_dict[k] = min(0, v)
        res = []
        for k, v in ch_dict.items():
            res += [k] * v
        return res

