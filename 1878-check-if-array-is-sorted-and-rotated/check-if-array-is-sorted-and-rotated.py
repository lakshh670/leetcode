class Solution:
    def check(self, nums: List[int]) -> bool:
        # There can only be one point(pivot) where elements are first decreasing and then increasing.
        # ex: [5,4,3,1,2] This can never be sorted.
        count=0
        n=len(nums)
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                count+=1
        if nums[n-1]>nums[0]:
            count+=1
        return True if count<=1 else False

        