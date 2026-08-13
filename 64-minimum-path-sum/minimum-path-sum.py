class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dp=[[-1]*n for _ in range(m)]
        def solve(i,j):
            if i==m-1 and j==n-1:
                return grid[m-1][n-1]
            
            if  dp[i][j]!=-1:
                return dp[i][j]
            path1,path2=float('inf'),float('inf')
            if i+1<m:
                path1=grid[i][j]+solve(i+1,j)
            if j+1<n:
                path2=grid[i][j]+solve(i,j+1)
            dp[i][j]=min(path1,path2)
            return dp[i][j]
        return solve(0,0)
        
        