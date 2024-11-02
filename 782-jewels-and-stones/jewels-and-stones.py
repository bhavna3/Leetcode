class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set()
        count = 0
        for j in jewels:
            s.add(j)
        for st in stones:
            if st in s:
                count += 1
        return count  