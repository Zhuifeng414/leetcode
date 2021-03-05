class Solution:
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0

        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        for item in envelopes:
            print(item)

        f = [1] * n
        for i in range(n):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    f[i] = max(f[i], f[j] + 1)
        print(f)
        return max(f)

if __name__ == '__main__':
    envelopes = [[5,4],[6,4],[6,7],[2,3],[5,5]]
    print(Solution().maxEnvelopes(envelopes))
