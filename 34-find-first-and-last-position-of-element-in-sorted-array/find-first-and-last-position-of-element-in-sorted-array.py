# In sorted data structures, lower bound is the index of the first element greater than or equal to a target value, while upper bound is the index of the first element strictly greater than the target value.
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        if not nums or target>nums[-1] or target<nums[0]:
            return [-1,-1]
        def lower_bound():
            left,right=0,n-1
            while left<=right:
                mid=left+(right-left)//2
                if nums[mid]>=target:
                    right=mid-1
                else:
                    left=mid+1
            return left if nums[left]==target else -1

        def upper_bound():
            left,right=0,n-1
            while left<=right:
                mid=left+(right-left)//2
                if nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return right if nums[right]==target else -1
        return [lower_bound(),upper_bound()]
        