class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res,curr_sum=float('-inf'),0
        for x in nums:
            res=max(res,curr_sum+x)
            if curr_sum<-x:
                
                curr_sum=0
            else:
                curr_sum+=x
                
                
        return res
        