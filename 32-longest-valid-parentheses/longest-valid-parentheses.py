class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        l=['0']*len(s)
        for indx,i in enumerate(s):
            if i=='(':
                stack.append(indx)
            else:
                if stack:
                    l[stack.pop()]='1'
                    l[indx]='1'
        return max(len(i) for i in ''.join(l).split('0'))