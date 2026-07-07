class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len=0
        i,j=0,0
        n=len(nums)
        while j<n:
            if nums[j]==1:
                max_len=max(max_len,j-i+1)
                
            else:
                i=j+1
            j+=1
        
        return max_len

        