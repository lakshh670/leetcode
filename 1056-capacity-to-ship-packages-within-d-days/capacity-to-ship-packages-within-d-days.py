class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def check(k_cap):
            count=0
            s=0
            for x in weights:
                if x>k_cap:
                    return False
                if s+x>k_cap:
                    count+=1
                    s=0
                s+=x
            return count+1<=days
        left,right=min(weights),sum(weights)
        res=right
        while left<=right:
            mid=left+(right-left)//2
            if check(mid):
                res=mid
                right=mid-1
            else:
                left=mid+1
        return res
