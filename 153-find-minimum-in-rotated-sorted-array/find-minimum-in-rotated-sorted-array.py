class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left,right=0,len(nums)-1
        
        while left<=right:
            mid=left+(right-left)//2
            if left==mid:
                left+=1
                continue
            if nums[mid]>nums[left]:
                left=mid
            else:
                right=mid
        if left==len(nums):
            return nums[-1] if nums[-1]<nums[0] else nums[0]
        return nums[left-1]
        