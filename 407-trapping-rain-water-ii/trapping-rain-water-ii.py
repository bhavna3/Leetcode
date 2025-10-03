class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])

        if m < 3 or n < 3:
            return 0
			
        min_heap = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1
					
        l, res = 0, 0
        while min_heap:
            h, x, y = heapq.heappop(min_heap)
            l = max(h, l)

            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= i < m and 0 <= j < n and heightMap[i][j] != -1:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
					
                    if heightMap[i][j] < l:
                        res += l - heightMap[i][j]
						
                    heightMap[i][j] = -1
        return res