class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n=len(intervals)
        for i in range(n):
            intervals[i].append(i)
        res=[-1]*n
        intervals.sort()
        
        def check(i):
            l,r=i,n-1
            ans=-1
            while l<=r:
                mid=l+(r-l)//2
                if intervals[mid][0]>=intervals[i][1]:
                    ans=intervals[mid][2]
                    r=mid-1
                else:
                    l=mid+1
            return ans
        for i in range(n):
            index=check(i)
            res[intervals[i][2]]=index
        return res
        