class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        
        n = len(points)
        count = 0

        for i in range(n):
            up_y = points[i][1]
            low_y = float('-inf')

            for j in range(i + 1, n):
                curr_y = points[j][1]

                if curr_y <= up_y and curr_y > low_y:
                    count += 1
                    low_y = curr_y
                    
                    if curr_y == up_y:
                        break

        return count