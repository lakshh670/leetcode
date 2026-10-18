class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def check(k):
            count=0
            for x in piles:
                count+=1+(x-1)//k
            return count<=h
        maxi,mini=sum(piles),1
        res=maxi
        while mini<=maxi:
            mid=mini+(maxi-mini)//2
            if check(mid):
                res=mid
                maxi=mid-1
            else:
                mini=mid+1
        return res
        