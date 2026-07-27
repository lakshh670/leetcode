class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low,high,ans=0,len(nums)-1,len(nums)
        while low<=high:
            mid=low+(high-low)//2
            
            if nums[mid]<target:
                low=mid+1
            else:
                ans=mid
                high=mid-1
        return ans
        