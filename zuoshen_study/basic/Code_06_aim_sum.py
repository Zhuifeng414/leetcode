class AimSum():
    def __init__(self):
        return

    def process_aim(self, aim, arr, res, i):
        if i == len(arr):
            if res == aim:
                return True
            else:
                return False
        return (self.process_aim(aim, arr, res, i+1) or
        self.process_aim(aim, arr, res+arr[i], i+1))

    def dps(self, aim, arr):
        max_sum = 0
        for item in arr:
            max_sum += item
        dp = [[False for i in range(max_sum+1)] for i in range(len(arr)+1)]

        for i in range(max_sum+1):
            if i == aim:
                dp[len(arr)][i] = True
            else:
                dp[len(arr)][i] = False

        for i in range(len(arr)-1, -1, -1):
            for j in range(max_sum+1):
                if j+arr[i] > max_sum:
                    dp[i][j] = dp[i + 1][j]
                else:
                    dp[i][j] = dp[i+1][j] or dp[i+1][j+arr[i]]
        return dp[0][0]


if __name__ == '__main__':
    arr = [1, 2, 3]
    aim = 7
    #print(AimSum().process_aim(aim, arr, 0, 0))
    print(AimSum().dps(aim, arr))