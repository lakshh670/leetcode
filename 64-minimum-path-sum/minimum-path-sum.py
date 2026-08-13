class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        # dp=[[-1]*n for _ in range(m)]
        # def solve(i,j):
        #     if i==m-1 and j==n-1:
        #         return grid[m-1][n-1]
        #     if i==m or j==n:
        #         return float('inf')
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     dp[i][j]=grid[i][j]+min(solve(i+1,j),solve(i,j+1))
        #     return dp[i][j]
        # return solve(0,0)

        # dp=[[float('inf')]*(n+1) for _ in range(m+1)]
        # dp[m-1][n-1]=grid[m-1][n-1]
        # for i in range(m-1,-1,-1):
        #     for j in range(n-1,-1,-1):
        #         if i==m-1 and j==n-1:
        #             continue
        #         dp[i][j]=grid[i][j]+min(dp[i+1][j],dp[i][j+1])
        # return dp[0][0]

        forw=[float('inf')]*(n+1) 
        
        for i in range(m-1,-1,-1):
            curr=[float('inf')]*(n+1)
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    curr[j]=grid[i][j]
                    continue
                print(forw[j])
                curr[j]=grid[i][j]+min(forw[j],curr[j+1])
            forw=curr
        return forw[0]
        
        