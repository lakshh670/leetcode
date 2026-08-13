class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        # dp=[[-1]*2 for _ in range(n)]
        # def solve(i,flag):
        #     if i==n-1:
        #         if flag:
        #             return nums[i]
        #         else:
        #             return 0
                
        #     if dp[i][flag]!=-1:
        #         return dp[i][flag]
        #     option1,option2=0,0
        #     if flag:
        #         option1=nums[i]+solve(i+1,0)
        #     option2=solve(i+1,1)
        #     dp[i][flag]=max(option1,option2)
        #     return dp[i][flag]
        # return solve(0,1)

        # dp=[-1]*n
        # def solve(i):
        #     if i>=n:
        #         return 0
        #     if dp[i]!=-1:
        #         return dp[i]
        #     want=nums[i]+solve(i+2)
        #     not_want=solve(i+1)
        #     dp[i]=max(want,not_want)
        #     return dp[i]
        # return solve(0)

        dp=[-1]*(n+2)
        dp[-1],dp[-2]=0,0
        for i in range(n-1,-1,-1):
            want=nums[i]+dp[i+2]
            not_want=dp[i+1]
            dp[i]=max(want,not_want)
        return dp[0]

        # We can also solve this using 1D dp.
        

        