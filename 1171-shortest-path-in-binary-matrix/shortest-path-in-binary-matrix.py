import heapq
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        dist={}
        dist[(0,0)]=1
        q=[]
        heapq.heappush(q,(1,(0,0)))
        while q:
            dis,(x,y)=heapq.heappop(q)
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
                if 0<=x+dx<len(grid) and 0<=y+dy<len(grid[0]) and grid[x+dx][y+dy]==0:
                    if (x+dx,y+dy) not in dist or dist[(x+dx,y+dy)]>1+dis:
                        dist[(x+dx,y+dy)]=1+dis
                        heapq.heappush(q,(1+dis,(x+dx,y+dy)))
        return dist[(len(grid)-1,len(grid[0])-1)] if (len(grid)-1,len(grid[0])-1) in dist else -1
        
        
        