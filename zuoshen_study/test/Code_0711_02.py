
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        import heapq
        m = len(heightMap)
        n = len(heightMap[0])
        visit = [[0 for i in range(n)] for j in range(m)]
        cache = []
        for j in range(n-1):
            i = 0
            cache.append((heightMap[i][j], i, j))
            visit[i][j] = 1
            #print(heightMap[i][j], i, j)
        for i in range(m-1):
            j = n-1
            cache.append((heightMap[i][j], i, j))
            visit[i][j] = 1
            #print(heightMap[i][j], i, j)
        for j in range(n-1, 0, -1):
            i = m-1
            cache.append((heightMap[i][j], i, j))
            visit[i][j] = 1
            #print(heightMap[i][j], i, j)
        for i in range(m-1, 0, -1):
            j = 0
            cache.append((heightMap[i][j], i, j))
            visit[i][j] = 1
            #print(heightMap[i][j], i, j)

        heapq.heapify(cache)
        max_v = float('-inf')
        rain_amount = 0
        while len(cache) > 0:
            [v, x0, y0] = heapq.heappop(cache)
            max_v = max(max_v, v)
            for [xs, ys] in ([[x0-1, y0], [x0+1, y0], [x0, y0-1], [x0, y0+1]]):
                if (0 <= xs <= m-1) and (0 <= ys <= n-1) and (visit[xs][ys] == 0):
                    vs = heightMap[xs][ys]
                    if vs < max_v:
                        rain_amount += (max_v - vs)
                    heapq.heappush(cache, (heightMap[xs][ys], xs, ys))
                    visit[xs][ys] = 1
        return rain_amount

heightMap = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

res = Solution().trapRainWater(heightMap)
print(res)

