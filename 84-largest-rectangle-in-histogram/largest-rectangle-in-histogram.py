class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n=len(heights)
        next_smaller=[n-1]*n
        prev_smaller=[0]*n
        st=[]
        for i in range(n-1,-1,-1):
            while st and heights[st[-1]]>=heights[i]:
                st.pop()
            if st:
                next_smaller[i]=st[-1]-1
            st.append(i)
        st=[]
        for i in range(n):
            while st and heights[st[-1]]>=heights[i]:
                st.pop()
            if st:
                prev_smaller[i]=st[-1]+1
            st.append(i)
        res=0
        
        for i in range(n):
            curr_area=(next_smaller[i]-prev_smaller[i]+1)*heights[i]
            res=max(res,curr_area)
        return res
