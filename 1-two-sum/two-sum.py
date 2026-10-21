class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]

        dic={}
        
        for i in range(n):
            
            if target-nums[i] in dic:
                return [dic[target-nums[i]],i]
            dic[nums[i]]=i
            