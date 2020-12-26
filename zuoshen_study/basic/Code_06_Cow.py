class Cow():
    def __init__(self):
        return

    def cowNumber(self, n):
        if n < 1:
            return 0
        if n <= 3:
            return n
        return self.cowNumber(n-1) + self.cowNumber(n-3)

    def dps(self, n):
        dp = [0 for i in range(n+1)]
        for i in range(4):
            dp[i] = i

        if n <= 3:
            return dp[n]

        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-3]

        return dp[n]

if __name__ == '__main__':
    n = 4
    #print(Cow().cowNumber(n))
    print(Cow().dps(6))