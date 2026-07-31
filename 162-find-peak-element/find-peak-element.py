class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Brute Force
        # if len(nums)==1:
        #     return 0
        # nums.append(float('-inf'))
        # i=1
        # while i<len(nums)-1:
        #     if nums[i-1]<nums[i]>nums[i+1]:
        #         return i
        #     i+=1
        # return 0

        # Modified binary search
        left,right=0,len(nums)-1
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]>nums[mid+1]:
                right=mid
            else:
                left=mid+1
        return left

        