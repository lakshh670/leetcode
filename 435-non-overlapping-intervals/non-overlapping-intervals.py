class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        n=len(intervals)
        prev_end=intervals[0][1]
        count=0
        for i in range(1,n):
            if intervals[i][0]<prev_end:
                count+=1
                prev_end=min(prev_end,intervals[i][1])
            else:
                prev_end=intervals[i][1]
        return count
        

        