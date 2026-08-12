class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        l1,l2,l3=len(s1),len(s2),len(s3)
        if l3!=l1+l2:
            return False
        dp=[[[-1]*l3 for _ in range(l2)] for _ in range(l1)]
        def solve(i,j,k):
            if i==l1:
                return s3[k:]==s2[j:]
            if j==l2:
                return s3[k:]==s1[i:]
            if dp[i][j][k]!=-1:
                return dp[i][j][k]
            option1,option2=False,False
            if s1[i]==s3[k]:
                
                option1=solve(i+1,j,k+1)
            if s2[j]==s3[k]:    

                option2=solve(i,j+1,k+1)
            dp[i][j][k]= option1 or option2
            return dp[i][j][k]
        return solve(0,0,0)
            
        