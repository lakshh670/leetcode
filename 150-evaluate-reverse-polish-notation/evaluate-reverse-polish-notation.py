class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        operand={
            '+':operator.add,
            '*':operator.mul,
            '-':operator.sub,
            '/':lambda a,b:int(a/b)
        }
        
        st=[]
        for x in tokens:
            if x in operand:
                a,b=st.pop(),st.pop()
                st.append(operand[x](b,a))
            else:
                st.append(int(x))
        return st[-1]
        