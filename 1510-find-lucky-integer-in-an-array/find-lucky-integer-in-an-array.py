from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)  
        lucky_num = -1

        for num, count in freq.items():
            if num == count:
                lucky_num = max(lucky_num, num)

        return lucky_num