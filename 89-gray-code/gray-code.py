class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]

        for i in range(n):
            for k in reversed(res):
                res.append(k | (1 << i))
                
        return res