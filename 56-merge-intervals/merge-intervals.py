class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        res=[]
        intervals.sort()
        for x in intervals:
            if  res and res[-1][1]>=x[0]:
                left=res[-1][0]
                right=max(res[-1][1],x[1])
                res.pop()
                res.append([left,right])
            else:
                res.append(x)
        return res
        