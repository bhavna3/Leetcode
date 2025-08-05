class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        i = 0
        while i < len(fruits):
            j = 0
            while j < len(baskets):
                if fruits[i] <= baskets[j]:
                    baskets[j]=0
                    break
                else:
                    j+=1
            i+=1
        
        res = 0
        for i in baskets:
            if i == 0:
                res += 1
        
        return len(baskets) - res
