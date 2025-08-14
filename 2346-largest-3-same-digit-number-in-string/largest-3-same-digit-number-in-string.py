class Solution:
    def largestGoodInteger(self, num: str) -> str:
        s='0'
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                s=max(s,num[i:i+3])
        return "" if s=='0' else s

        