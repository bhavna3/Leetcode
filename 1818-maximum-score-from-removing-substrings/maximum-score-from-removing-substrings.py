class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove(pair,score):
            nonlocal s
            stack=[]
            res=0

            for ch in s:
                if ch==pair[1] and stack and stack[-1]==pair[0]:
                    stack.pop()
                    res+=score
                else:
                    stack.append(ch)

            s=''.join(stack)
            return res

        res=0
        pair='ab' if x>y else 'ba'
        res+=remove(pair,max(x,y))
        res+=remove(pair[::-1],min(x,y)) 
        return res
        