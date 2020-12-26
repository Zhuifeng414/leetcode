class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        if start < 0 or start >= len(arr):
            return False
        if arr[start] == 0:
            return True
        return self.process(arr, start)

    def process(self, arr, start):
        if arr[start] == 0:
            return True

        tmp = 1
        for item in arr:
            if item == 0:
                tmp = 0
                break
        if tmp == 1:
            return False

        dp = [False for i in range(len(arr))]
        stack = [start]
        dp[start] = True
        p1 = False
        p2 = False

        while len(stack) > 0 :
            start = stack.pop(0)
            dp[start] = True

            if 0 <= start + arr[start] <= len(arr) - 1:
                p1 = dp[start + arr[start]]
            else:
                p1 = True

            if 0 <= start - arr[start] <= len(arr) - 1:
                p2 = dp[start - arr[start]]
            else:
                p2 = True

            if p1 is False:
                stack.append(start + arr[start])
            if p2 is False:
                stack.append(start - arr[start])

        for i in range(len(arr)):
            if dp[i] is True:
                if arr[i] == 0:
                    return True
        return False

if __name__ == '__main__':
    arr = [4, 4, 1, 3, 0, 3]
    start = 2
    res = Solution().canReach(arr, start)