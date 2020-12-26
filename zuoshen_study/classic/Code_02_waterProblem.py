class WaterProblem:
    def __init__(self):
        return

    def getWater_slow(self, arr):
        N = len(arr)
        if N < 3:
            return 0
        n = N - 2
        rightMaxs = [0 for i in range(n)]
        rightMaxs[n - 1] = arr[n + 1]
        for i in range(n-2, -1, -1):
            rightMaxs[i] = max(rightMaxs[i + 1], arr[i + 2])
        leftMax = arr[0]
        value = 0
        for i in range(n+1):
            value += max(0, min(leftMax, rightMaxs[i - 1]) - arr[i])
            leftMax = max(leftMax, arr[i])
        return value


    def getWater_fast(self, arr):
        N = len(arr)
        if N < 3:
            return 0
        value = 0
        leftMax = arr[0]
        rightMax = arr[N - 1]
        l = 1
        r = N - 1
        while l <= r:
            if leftMax <= rightMax:
                value += max(0, leftMax - arr[l])
                leftMax = max(leftMax, arr[l])
                l += 1
            else:
                value += max(0, rightMax - arr[r])
                rightMax = max(rightMax, arr[r])
                r -= 1
        return value

if __name__ == '__main__':
    arr = [2, 3, 1, 4, 5]
    print('slow: ', WaterProblem().getWater_slow(arr))
    print('fast: ', WaterProblem().getWater_fast(arr))

