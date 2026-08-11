class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp=[[-1]*len(word2) for _ in range(len(word1))]
        # def solve(i,j):
        #     if word1[i:]==word2[j:]:
        #         return 0
        #     if i==len(word1):
        #         return len(word2[j:])
        #     if j==len(word2):
        #         return len(word1[i:])
        #     if dp[i][j]!=-1:
        #         return dp[i][j]


        #     if word1[i]==word2[j]:
        #         dp[i][j]= solve(i+1,j+1)
        #     else:
        #         replace=1+solve(i+1,j+1) # imagine we have replaced the ith index of word1 with a character which will match with the jth index charac of word2. Now i and j are equal so we can increament the both.
        #         delete=1+solve(i+1,j)
        #         insert=1+solve(i,j+1)
        #         dp[i][j] =min(replace,delete,insert)
        #     return dp[i][j]
        # return solve(0,0)


        # dp=[[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        # for j in range(len(word2)):
        #     dp[len(word1)][j]=len(word2[j:])
        # for i in range(len(word1)+1):
        #     dp[i][len(word2)]=len(word1[i:])
        # for i in range(len(word1)-1,-1,-1):
        #     for j in range(len(word2)-1,-1,-1):
        #         if word1[i]==word2[j]:
        #             dp[i][j]=dp[i+1][j+1]
        #         else:
        #             insert=1+dp[i][j+1]
        #             delete=1+dp[i+1][j]
        #             replace=1+dp[i+1][j+1]
        #             dp[i][j]=min(insert,delete,replace)
        # return dp[0][0]


        forw=[0]*(len(word2)+1) 
        for j in range(len(word2)):
            forw[j]=len(word2[j:])
        
        for i in range(len(word1)-1,-1,-1):
            curr=[0]*(len(word2)+1)
            curr[len(word2)]=len(word1[i:])
            for j in range(len(word2)-1,-1,-1):
                
                if word1[i]==word2[j]:
                    curr[j]=forw[j+1]
                else:
                    insert=1+curr[j+1]
                    delete=1+forw[j]
                    replace=1+forw[j+1]
                    curr[j]=min(insert,delete,replace)
            forw=curr
        return forw[0]
        