import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if x < y:
                heapq.heappush(heap, x-y)
        if heap:
            return -heap[0]
        return 0

