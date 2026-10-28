class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        # operand={
        #     '+':operator.add,
        #     '*':operator.mul,
        #     '-':operator.sub,
        #     '/':lambda a,b:int(a/b)
        # }
        
        # st=[]
        # for x in tokens:
        #     if x in operand:
        #         a,b=st.pop(),st.pop()
        #         st.append(operand[x](b,a))
        #     else:
        #         st.append(int(x))
        # return st[-1]

        st = []

        for c in tokens:
            if c == "+":
                st.append(st.pop() + st.pop())
            elif c == "-":
                second, first = st.pop(), st.pop()
                st.append(first - second)
            elif c == "*":
                st.append(st.pop() * st.pop())
            elif c == "/":
                second, first = st.pop(), st.pop()
                st.append(int(first / second))                
            else:
                st.append(int(c))
        
        return st[0]
        