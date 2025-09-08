class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(n):
            a=i
            b=n-i
            if not ('0' in str(a) or '0' in str(b)):
                return [a,b]
        