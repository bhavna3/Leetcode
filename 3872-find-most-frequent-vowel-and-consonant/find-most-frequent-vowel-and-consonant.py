class Solution:
    def maxFreqSum(self, s: str) -> int:
        vow_set=set('aeiou')
        
        freq=Counter(s)

        vow=[count for ch,count in freq.items() if ch in vow_set]
        cons=[count for ch,count in freq.items() if ch not in vow_set]

        max_vow=max(vow) if vow else 0
        max_cons=max(cons) if cons else 0

        return max_vow+max_cons

        