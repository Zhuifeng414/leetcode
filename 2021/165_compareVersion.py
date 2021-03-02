class Solution(object):
    def del_0(self, sub_str):
        index = 0
        for i in range(len(sub_str)):
            if sub_str[i] == '0':
                index += 1
            else:
                break
        sub_str = sub_str[index:]
        if sub_str == '':
            return 0
        else:
            return int(sub_str)

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ver1 = [self.del_0(item) for item in version1.split('.')]
        ver2 = [self.del_0(item) for item in version2.split('.')]
        max_len = max(len(ver1), len(ver2))
        for i in range(max_len):
            sver1 = ver1[i] if i < len(ver1) else 0
            sver2 = ver2[i] if i < len(ver2) else 0
            if sver1 > sver2:
                return 1
            elif sver1 < sver2:
                return -1
            elif sver1 == sver2:
                continue
        return 0