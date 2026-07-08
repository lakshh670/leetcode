class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i,j=0,0
        while j<n:
            if nums[j]==0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1
        j=i
        while j<n:
            if nums[j]==1:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1

        j=i
        while j<n:
            if nums[j]==2:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1
        

        