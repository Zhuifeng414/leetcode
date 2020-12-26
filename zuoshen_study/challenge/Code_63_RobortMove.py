class Solution(object):
    def __init__(self, N, M, K , P):
        self.N = N
        self.M = M
        self.K = K
        self.P = P
        return

    def process(self, index, pos):
        if index == self.K:
            if pos == self.P:
                return 1
            else:
                return 0
        if index > self.K:
            return 0
        if pos == 1:
            return self.process(index+1, pos+1)
        if pos == self.N:
            return self.process(index+1, pos-1)
        #print('h~~~')
        return self.process(index+1, pos+1) + self.process(index+1, pos-1)

    def dps(self):
        dp = [[0 for i in range(self.N)] for j in range(self.K+1)]
        dp[0][self.M] = 1
        # for item in dp:
        #     print(item)
        for i in range(1, self.K+1):
            for j in range(self.N):
                p1 = dp[i-1][j+1] if j+1<=self.N-1 else 0
                p2 = dp[i-1][j-1] if j-1>=0 else 0
                dp[i][j] = p1 + p2
        # print('>>>>=============>>>>')
        # for item in dp:
        #     print(item)
        return dp[self.K][self.P]

    def dps_zip(self):
        dp = [0 for i in range(self.N)]
        dp[self.M] = 1
        for i in range(1, self.K+1):
            leftUp = dp[0]
            #print(dp)
            for j in range(self.N):
                tmp = dp[j]
                p1 = dp[j+1] if j+1<=self.N-1 else 0
                p2 = leftUp if j-1>=0 else 0
                dp[j] = p1 + p2
                leftUp = tmp
        # print('>>>>=============>>>>')
        #print(dp)
        return dp[self.P]

if __name__ == '__main__':
    N = 5
    M = 2
    K = 3
    P = 3
    pos = M
    index = 0
    print(Solution(N, M, K, P).process(index, pos))
    print('================>')
    print(Solution(N, M, K, P).dps())
    print('================>')
    print(Solution(N, M, K, P).dps_zip())