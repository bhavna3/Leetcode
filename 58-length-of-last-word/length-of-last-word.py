class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st = s.split()
        return len(st[-1])