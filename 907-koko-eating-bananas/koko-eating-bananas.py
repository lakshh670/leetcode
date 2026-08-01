import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)

        def check(num):
            s=0
           
            for x in piles:
                s+=math.ceil(x/num)
            return True if s<=h else False

        while left<right:
            mid=left+(right-left)//2
            if check(mid):
                right=mid
            else:
                left=mid+1
        return left
        