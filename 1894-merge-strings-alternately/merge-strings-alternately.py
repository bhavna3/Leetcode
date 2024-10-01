class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ls = []
        
        for a, b in zip(word1, word2):
            ls.append(a)
            ls.append(b)
        
        if len(word1) > len(word2):
            ls.append(word1[len(word2):])  
        elif len(word2) > len(word1):
            ls.append(word2[len(word1):])  
        
        return "".join(ls)