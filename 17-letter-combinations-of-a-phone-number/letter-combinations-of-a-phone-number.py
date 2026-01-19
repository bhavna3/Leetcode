class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]


        if not digits: return res
        
        mapp = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(id, cur):
            nonlocal res
            if id == len(digits):
                res.append(cur)
                return
            
            digit = digits[id]
            letters = mapp[digit]
            for letter in letters:
                backtrack(id + 1, cur + letter)
        
        backtrack(0, "")
        return res