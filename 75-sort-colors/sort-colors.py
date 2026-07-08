class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        # i,j=0,0
        # while j<n:
        #     if nums[j]==0:
        #         nums[i],nums[j]=nums[j],nums[i]
        #         i+=1
        #     j+=1
        # j=i
        # while j<n:
        #     if nums[j]==1:
        #         nums[i],nums[j]=nums[j],nums[i]
        #         i+=1
        #     j+=1

        # j=i
        # while j<n:
        #     if nums[j]==2:
        #         nums[i],nums[j]=nums[j],nums[i]
        #         i+=1
        #     j+=1

        # Dutch National Flag algorithm
        low,mid,high=0,0,n-1
        while mid<=high: # Remember this, it's not mid<n
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1 # We wont update mid if we get 2
            
        

        