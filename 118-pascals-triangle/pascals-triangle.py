
class Solution:
    def generate_row(self, row: int) -> List[int]:
        ans = 1
        ls = [1]  
        for i in range(1, row + 1):
            ans = ans * (row - i + 1) // i   
            ls.append(ans)
        return ls

    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):  
            res.append(self.generate_row(i))
        return res
            


        