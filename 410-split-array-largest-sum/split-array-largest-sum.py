class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        dp=[[-1]*(k+1) for _ in range(len(nums)+1)]
        def dfs(i,k):
            if k==1:
                return sum(nums[i:])
            if dp[i][k]!=-1:
                return dp[i][k]
            res,curr_sum=float('inf'),0
            for j in range(i,len(nums)-k+1):
                curr_sum+=nums[j]
                max_sum=max(curr_sum,dfs(j+1,k-1))
                res=min(res,max_sum)
                if max_sum>res:
                    break
            dp[i][k]=res
            return dp[i][k]
        return dfs(0,k)
        