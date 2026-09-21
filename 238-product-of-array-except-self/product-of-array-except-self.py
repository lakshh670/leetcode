class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        forw_pro,back_pro=[1]*n,[1]*n
        prod=1
        for i in range(n-1):
            prod*=nums[i]
            forw_pro[i+1]=prod
        prod=1
        for i in range(n-1,0,-1):
            prod*=nums[i]
            back_pro[i-1]=prod
        res=[]
        for i in range(n):
            res.append(forw_pro[i]*back_pro[i])
        return res

        