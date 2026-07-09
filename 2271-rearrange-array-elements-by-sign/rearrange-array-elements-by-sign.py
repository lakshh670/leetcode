class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_left,neg_left=0,1
        right=0
        n=len(nums)
        ans=[1]*n
        while right<n:
            if nums[right]>0:
                ans[pos_left]=nums[right]
                pos_left+=2
            else:
                ans[neg_left]=nums[right]
                neg_left+=2
            right+=1
        return ans