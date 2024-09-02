class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for word in s:
            return len(s.split()[-1])