class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res_dict = {}
        for item in strs:
            #print(item)
            sub = ''.join(sorted(item))
            #print(sub)
            if sub in res_dict.keys():
                res_dict[sub].append(item)
            else:
                res_dict[sub] = [item]
        return list(res_dict.values())

if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    res = Solution().groupAnagrams(strs)
    print(res)