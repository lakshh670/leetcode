class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return
        if len(nums)==2:
            if nums[0]>nums[1]:
                nums.sort()
            else:
                nums[0],nums[1]=nums[1],nums[0]
            return

        n=len(nums)
        idx=n-2
        while idx>=0:
            if nums[idx]<nums[idx+1]:
                break
            idx-=1
        if idx==-1:
            nums.sort()
            return
        swap_idx=n-1
        while swap_idx>idx:
            if nums[swap_idx]>nums[idx]:
                break
            swap_idx-=1
        nums[idx],nums[swap_idx]=nums[swap_idx],nums[idx]
        nums[idx+1:]=sorted(nums[idx+1:])

                
        