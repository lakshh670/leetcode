class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res=set()

        # for i in range(len(nums)):
        #     tar=-nums[i]
        #     hash_={}
        #     ans=[]
        #     for j in range(i+1,len(nums)):
                
        #         if tar-nums[j] in hash_:
        #             res.add(tuple(sorted([nums[i],tar-nums[j],nums[j]])))
        #         hash_[nums[j]]=j
            
        # return [list(x) for x in res]

        nums.sort()
        n=len(nums)
        i=0
        while i<n:
            j=i+1
            k=n-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    res.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
                else:
                    k-=1
            i+=1
        return [list(x) for x in res]   



        