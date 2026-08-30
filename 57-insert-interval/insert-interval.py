class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort()
        
        ans=[]
        for x,y in intervals:
            if not ans or ans[-1][1]<x:
                ans.append([x,y])
            else:
                i,j=ans.pop()
                ans.append([min(i,x),max(j,y)])
        return ans

        