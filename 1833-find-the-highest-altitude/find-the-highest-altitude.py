class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt= 0
        curAlt = 0
        
        for g in gain:
            curAlt += g
            maxAlt = max(maxAlt, curAlt)
        
        return maxAlt