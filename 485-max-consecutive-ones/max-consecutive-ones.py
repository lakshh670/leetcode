class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        # Approach 1
        # max_len=0
        # i,j=0,0
        # n=len(nums)
        # while j<n:
        #     if nums[j]==1:
        #         max_len=max(max_len,j-i+1)
                
        #     else:
        #         i=j+1
        #     j+=1
        
        # return max_len

        # Approach 2
        res,count=0,0
        for x in nums:
            if x==0:
                count=0
            else:
                count+=1
                res=max(res,count)
        return res

        