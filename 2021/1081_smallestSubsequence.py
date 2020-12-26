import collections

class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen = set()
        letter_dict = collections.Counter(s)
        res = []
        for item in s:
            if item not in seen:
                while res and (res[-1] > item) and (letter_dict[res[-1]] > 0):
                    seen.discard(res.pop())
                res.append(item)
                seen.add(item)
            letter_dict[item] -= 1
        return ''.join(res)

if __name__ == '__main__':
    s = "cdadabcc"
    print(Solution().smallestSubsequence(s))
