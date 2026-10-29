class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n=len(num)
        st=[]
        for digit in num:
            while st and digit<st[-1] and k:
                st.pop()
                k-=1
            
            st.append(digit)
        while k : # This loop is important
            st.pop()
            k-=1
        ans="".join(st).lstrip('0')
        return ans if ans else "0"

        
        
            
        