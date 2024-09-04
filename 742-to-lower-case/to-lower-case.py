class Solution:
    def toLowerCase(self, s: str) -> str:
        res = []

        for char in s:
            if char.isupper():
                res.append(char.lower())
            else:
                res.append(char)
        
        # return the final string
        return ''.join(res)       
        