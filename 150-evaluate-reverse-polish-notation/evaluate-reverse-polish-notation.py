class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        st=[]
        opt={'+','-','*','/'}
        for s in tokens:
            if s not in opt:
                st.append(int(s))
            else:
                if st:
                    exp1=st.pop()
                    exp2=st.pop()
                    if s=='+':
                        val=exp2+exp1
                    elif s=='-':
                        val=exp2-exp1
                    elif s=='*':
                        val=exp2*exp1
                    elif s=='/':
                        val=int(float(exp2)/exp1)

                st.append(val)
        return st[0]


