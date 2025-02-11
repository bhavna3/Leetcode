class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        maxHeap = []
        
        for point in points:
            heapq.heappush(maxHeap, (self.getDistance(point), point))

        result = [heapq.heappop(maxHeap)[1] for _ in range(k)]
        return result

    def getDistance(self, point):
        return math.sqrt(point[0] ** 2 + point[1] ** 2)