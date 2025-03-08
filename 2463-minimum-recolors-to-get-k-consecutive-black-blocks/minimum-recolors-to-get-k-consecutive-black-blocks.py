class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        count=0
        n=len(blocks)
        for i in range(0,k):
            if blocks[i]=='W':
                count+=1

        cnt=count
        for i in range(k, n):
            if blocks[i-k]=='W':
                count-=1
            if blocks[i]=='W':
                count+=1
            cnt=count if count<cnt else cnt
        
        return cnt

         
        


        