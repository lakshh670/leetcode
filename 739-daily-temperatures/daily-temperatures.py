class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n=len(temperatures)
        next_greater=[-1]*n
        st=[]
        for i in range(n-1,-1,-1):
            while st and temperatures[st[-1]]<=temperatures[i]:
                st.pop()
            if st:
                next_greater[i]=st[-1]
            st.append(i)
        res=[0]*n
        for i in range(n):
            if next_greater[i]!=-1:
                res[i]=next_greater[i]-i
        return res

        