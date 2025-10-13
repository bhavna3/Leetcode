class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n=len(words)

        s=[''.join(sorted(w)) for w in words]
        ans=[words[0]]

        for i in range(1,n):
            if s[i]!=s[i-1]:
                ans.append(words[i])
        return ans
        