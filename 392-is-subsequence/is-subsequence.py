class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        S=len(s)
        T=len(t)

        if s=="": return True
        if T<S: return False

        j=0
        for i in range(T):
            if s[j]==t[i]:
                if j==S-1:
                    return True
                j+=1
        return False

        # t.c. O(T)
        # s.c. O(1)


        