class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        start_h=1001
        end_h=-1
        start_w=1001
        end_w=-1

        rows=grid
        cols=grid[0]

        for r in range(len(rows)):
            for c in range(len(cols)):
                if grid[r][c]==1:
                    start_h=min(start_h,r)
                    end_h=max(end_h,r)
                    start_w=min(start_w,c)
                    end_w=max(end_w,c)

        return (end_h-start_h+1)*(end_w-start_w+1)
        