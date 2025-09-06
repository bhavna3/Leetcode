class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        res=0

        for l, r in queries:
            temp=0
            start=1
            end=4
            for d in range(1,16):
                left=max(l,start)
                right=min(r,end-1)
                if right>=left:
                    temp=temp+(right-left+1)*d
                start*=4
                end*=4
            res+=ceil(temp/2)
        return res
        