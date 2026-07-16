class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        q=deque()
        for i in range(rows):
            if grid[i][0]==1:
                q.append((i,0))
                grid[i][0]=0
            if grid[i][cols-1]==1:
                q.append((i,cols-1))
                grid[i][cols-1]=0
        for j in range(cols):
            if grid[0][j]==1:
                q.append((0,j))
                grid[0][j]=0
            if grid[rows-1][j]==1:
                q.append((rows-1,j))
                grid[rows-1][j]=0
        

        while q:
            x,y=q.popleft()
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                if 0<=x+dx<rows and 0<=y+dy<cols and grid[x+dx][y+dy]==1:
                    q.append((x+dx,y+dy))
                    grid[x+dx][y+dy]=0
        print(grid)
        return sum([sum(row) for row in grid])

        
            
        