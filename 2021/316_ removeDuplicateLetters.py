import collections

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        letter_his = self.letter_his_sta(s)
        res_len = len(letter_his.keys())
        dup_res = [-1 for i in range(res_len)]
        dup_index = 0
        while (dup_index < res_len) and (len(s) > 0):
            letter_his = self.letter_his_sta(s)
            for i in range(len(s)):
                letter_item = s[i]
                letter_his[letter_item] -= 1
                if (letter_his[letter_item] == 0):
                    ## find min_letter and index
                    min_letter = min(s[:i + 1])
                    min_index = s.index(min_letter)
                    ## the new min_letter add to res
                    dup_res[dup_index] = min_letter
                    ## update string s and remove duplicate letter of min_letter
                    new_s = [item for item in s[min_index + 1:] if item != min_letter]
                    s = new_s
                    ## update dup_index
                    dup_index += 1
                    break
        return ''.join(dup_res)

    def letter_his_sta(self, s):
        letter_his = {}
        for item in s:
            if item in letter_his.keys():
                letter_his[item] += 1
            else:
                letter_his[item] = 1
        return letter_his

    def simple_removeDuplicateLetters(self, s):
        letter_dict = collections.Counter(s)
        seen = set()
        res = []
        for item in s:
            if item not in seen:
                while res and letter_dict[res[-1]] > 0 and item < res[-1]:
                    seen.discard(res.pop())
                res.append(item)
                seen.add(item)
            letter_dict[item] -= 1
        return ''.join(res)

if __name__ == '__main__':
    s = "cbacdcbc"
    res1 = Solution().removeDuplicateLetters(s)
    print(res1)
    res2 = Solution().simple_removeDuplicateLetters(s)
    print(res2)