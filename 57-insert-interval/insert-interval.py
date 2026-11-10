class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # intervals.append(newInterval)
        # intervals.sort()
        
        # ans=[]
        # for x,y in intervals:
        #     if not ans or ans[-1][1]<x:
        #         ans.append([x,y])
        #     else:
        #         i,j=ans.pop()
        #         ans.append([min(i,x),max(j,y)])
        # return ans


        # Better approach
        res=[]
        n=len(intervals)
        for i in range(n):
            if newInterval[1]<intervals[i][0]:
                res.append(newInterval)
                return res+intervals[i:]
            elif newInterval[0]>intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval=[min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
        res.append(newInterval)
        return res


        