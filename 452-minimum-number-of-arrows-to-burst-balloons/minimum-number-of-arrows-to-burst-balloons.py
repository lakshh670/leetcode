class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        n=len(points)
        res=n # initially we are assuming that each balloon neads an arrow.
        prev=points[0]
        for i in range(1,n):
            curr=points[i]
            if curr[0]<=prev[1]:
                res-=1 # We have found overlapping intervals, so now they can be bursted together i.e. we need to decreament the res.
                prev=[curr[0],min(prev[1],curr[1])]
            else:
                prev=curr
        return res
