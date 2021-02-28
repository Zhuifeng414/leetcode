class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        import collections
        wf = collections.Counter()
        for word in words:
            wbin = 0
            for ch in word:
                wbin |= 1 << (ord(ch) - ord('a'))
            if bin(wbin).count('1') <= 7:
                wf[wbin] += 1

        res = []
        for puzzle in puzzles:
            mask = 0
            for i in range(1, 7):
                mask |= 1 << (ord(puzzle[i]) - ord('a'))

            sub_set = mask
            sub_res = 0
            while sub_set:
                s = sub_set | (1 << (ord(puzzle[0]) - ord('a')))
                if s in wf:
                    sub_res += wf[s]
                sub_set = (sub_set - 1) & mask

            ## 空集额外判断
            if (1 << (ord(puzzle[0]) - ord("a"))) in wf:
                sub_res += wf[1 << (ord(puzzle[0]) - ord("a"))]

            res.append(sub_res)
        return res




