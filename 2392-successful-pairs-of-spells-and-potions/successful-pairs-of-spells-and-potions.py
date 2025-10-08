class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        n=len(potions)
        ans=[]

        for s in spells:
            l,r=0,n-1

            while l<=r:
                mid=(l+r)//2
                if potions[mid]*s>=success:
                    r=mid-1
                else:
                    l=mid+1

            ans.append(n-l)
        return ans
