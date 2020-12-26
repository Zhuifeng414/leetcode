class Node:
    def __init__(self, val=None, next=[], isEnd=False):
        self.val = val
        self.next = {i.val: i for i in next}
        self.isEnd = isEnd

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        tmp = self.node
        for i in word:
            if i not in tmp.next:
                tmp.next[i] = Node(i)
                tmp.next[i].val = 0
            tmp.next[i].val += 1
            tmp = tmp.next[i]
        tmp.isEnd = True

    def get_max(self, wn, subword):
        res = 0
        if len(self.node.next) == 1:
            root = self.node.next.values[0]
            while len(root) > 0:
                a = len(root.next)
                b = root.val
                if len(root.next) == 1 and root.val == wn:
                    res += 1
                    root = root.next.values[0]
                else:
                    break
            return subword[:res]
        else:
            return ''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pref = Trie()
        for item in strs:
            pref.insert(item)

        wn = len(strs)
        res = pref.get_max(wn, item)
        return res



strs = ["flower","flow","flight"]
res = Solution().longestCommonPrefix(strs)
print(res)

