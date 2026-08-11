class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1,l2=len(text1),len(text2)
        # dp=[[-1]*l2 for _ in range(l1)]
        # def solve(i,j):
        #     if i==l1 or j==l2:
        #         return 0
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     if text1[i]==text2[j]:
        #         dp[i][j]= 1+solve(i+1,j+1)
        #     else:
        #         dp[i][j]= max(solve(i,j+1),solve(i+1,j))
        #     return dp[i][j]
        # return solve(0,0)

        # dp=[[0]*(l2+1) for _ in range(l1+1)]
        # for i in range(l1-1,-1,-1):
        #     for j in range(l2-1,-1,-1):
        #         if text1[i]==text2[j]:
        #             dp[i][j]= 1+dp[i+1][j+1]
        #         else:
        #             dp[i][j]= max(dp[i][j+1],dp[i+1][j])
        # return dp[0][0]



        forw=[0]*(l2+1)
        for i in range(l1-1,-1,-1):
            curr=[0]*(l2+1)
            for j in range(l2-1,-1,-1):
                if text1[i]==text2[j]:
                    curr[j]= 1+forw[j+1]
                else:
                    curr[j]= max(curr[j+1],forw[j])
            forw=curr
        return forw[0]
        