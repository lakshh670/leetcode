class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # k=goal
        # res=0
        # dic=defaultdict(int)
        # s=0
        # dic[s]=1
        # for x in nums:
        #     s+=x
        #     if (s-k) in dic:
        #         res+=dic[s-k]
        #     dic[s]+=1
        # return res
        n=len(nums)
        def solve(k):
            cnt=0
            s=0
            l,r=0,0
            while r<n:
                s+=nums[r]
                while s>k and l<=r:
                    s-=nums[l]
                    l+=1
                if s<=k:
                    cnt+=r-l+1
                r+=1
            return cnt
        return solve(goal)-solve(goal-1)
