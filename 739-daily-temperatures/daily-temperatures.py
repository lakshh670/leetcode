class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Most optimal: Monotonic stack
        n=len(temperatures)
        res=[0]*n
        st=[]
        for i,x in enumerate(temperatures[::-1]):
            while st and st[-1][0]<=x:
                st.pop()
            res[n-1-i]=st[-1][1]-(n-1-i) if st else 0
            st.append([x,n-1-i])
        return res


        