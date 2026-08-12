class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        l1,l2,l3=len(s1),len(s2),len(s3)
        if l3!=l1+l2:
            return False
        # dp=[[-1]*(l2+1) for _ in range(l1+1)] 
        # def solve(i,j):
        #     if i==l1:
        #         return s3[i+j:]==s2[j:]
        #     if j==l2:
        #         return s3[i+j:]==s1[i:]
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     option1,option2=False,False
        #     if s1[i]==s3[i+j]:
                
        #         option1=solve(i+1,j)
        #     if s2[j]==s3[i+j]:    

        #         option2=solve(i,j+1)
        #     dp[i][j]= option1 or option2
        #     return dp[i][j]

        # return solve(0,0)

        # for j in range(l2):
        #     dp[l1][j]=s3[l1+j:]==s2[j:]
        # for i in range(l1):
        #     dp[i][l2]=s3[i+l2:]==s1[i:]
        # for i in range(l1-1,-1,-1):
        #     for j in range(l2-1,-1,-1):
        #         option1,option2=False,False
        #         if s1[i]==s3[i+j]:
                
        #             option1=dp[i+1][j]
        #         if s2[j]==s3[i+j]:    

        #             option2=dp[i][j+1]
        #         dp[i][j]= option1 or option2
        # return dp[0][0]

        forw=[-1]*(l2+1)
        for j in range(l2):
            forw[j]=s3[l1+j:]==s2[j:]
        
        for i in range(l1-1,-1,-1):
            curr=[-1]*(l2+1)
            curr[l2]=s3[l2+i:]==s1[i:]
            for j in range(l2-1,-1,-1):
                option1,option2=False,False
                if s1[i]==s3[i+j]:
                
                    option1=forw[j]
                if s2[j]==s3[i+j]:    

                    option2=curr[j+1]
                curr[j]= option1 or option2
            forw=curr
        return forw[0]
            
        