class Solution:
    def sortVowels(self, s: str) -> str:
        st = set("AEIOUaeiou")
        vowels = [c for c in s if c in st]
        vowels.sort()
        i = iter(vowels)

        result = []
        for c in s:
            result.append(next(i) if c in st else c)

        return ''.join(result)