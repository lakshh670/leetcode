class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        
        n=len(nums)
        res=0
        # Brute Force:
        # for l in range(n):
        #     dic=defaultdict(int)
        #     r=l
        #     while r<n and len(dic)<=k:
        #         dic[nums[r]]+=1
        #         if len(dic)==k:
        #             res+=1
                
        #         r+=1
        # return res

        dic=defaultdict(int)
        right,far_left,near_left=0,0,0
        while right<n:
            dic[nums[right]]+=1
            
            while len(dic)>k:
                dic[nums[near_left]]-=1
                if not dic[nums[near_left]]:
                    del dic[nums[near_left]]
                near_left+=1
                far_left=near_left
            while dic[nums[near_left]]>1:
                dic[nums[near_left]]-=1
                near_left+=1
            if len(dic)==k:
                res+=near_left-far_left+1
            right+=1
        return res

        