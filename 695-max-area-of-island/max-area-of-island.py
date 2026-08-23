class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        to_visit=set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    to_visit.add((i,j))
        q=deque()
        max_area=0
        while to_visit:
            q.append(to_visit.pop())
            area=0
            while q:
                x,y=q.popleft()
                grid[x][y]=0
                area+=1
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if 0<=x+dx<len(grid) and 0<=y+dy<len(grid[0]) and grid[x+dx][y+dy]:
                        grid[x+dx][y+dy]=0
                        q.append((x+dx,y+dy))
                        to_visit.remove((x+dx,y+dy))
            max_area=max(max_area,area)
        return max_area
            
        