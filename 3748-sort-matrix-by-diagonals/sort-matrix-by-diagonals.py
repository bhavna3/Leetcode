class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m=len(grid)

        def diag(r,c,order=True):
            arr=[]
            i,j=r,c
            while i<m and j<m:
                arr.append(grid[i][j])
                i+=1
                j+=1
            arr.sort(reverse=order)
            for val in arr:
                grid[r][c]=val
                r+=1
                c+=1
            

        #Lower
        for i in range(m):
            diag(i,0)

        #Upper
        for i in range(1,m):
            diag(0,i,order=False)

        return grid




        