class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # This will give MLE
        # q=deque()
        # count=0
        # q.append((0,0))
        # while q:
        #     x,y=q.popleft()
        #     if x==m-1 and y==n-1:
        #         count+=1
        #         continue
        #     for dx,dy in [(1,0),(0,1)]:
        #         if x+dx<m and y+dy<n:
        #             q.append((x+dx,y+dy))
        # return count

        # q=deque()
        # count=0
        # ways=[[0]*n for _ in range(m)]
        # ways[0][0]=1
        # q.append((0,0))
        # while q:
        #     x,y=q.popleft()
        #     if x+1<m:
        #         if ways[x+1][y]==0:
        #             q.append((x+1,y))
        #         ways[x+1][y]+=ways[x][y]
                
        #     if y+1<n:
        #         if ways[x][y+1]==0:
        #             q.append((x,y+1))
        #         ways[x][y+1]+=ways[x][y]
                
        # return ways[m-1][n-1]

        a=m+n-2
        b=m-1
        def fact(x):
            if x==1 or x==0:
                return 1
            return x*fact(x-1)
        return fact(a)//(fact(a-b)*fact(b))

        
        