import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left,right=1,max(nums)
        def check(x):
            s=0
            for num in nums:
                s+=math.ceil(num/x)
            return s<=threshold
        while left<right:
            mid=left+(right-left)//2
            if check(mid):
                right=mid
            else:
                left=mid+1
        return left
        