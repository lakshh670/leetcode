class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        orig_col=image[sr][sc]
        if orig_col==color:
            return image
        q=deque()
        q.append((sr,sc))
        image[sr][sc]=color
        while q:
            x,y =q.popleft()
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                if 0<=x+dx<len(image) and 0<=y+dy<len(image[0]) and image[x+dx][y+dy]==orig_col:
                    image[x+dx][y+dy]=color
                    q.append((x+dx,y+dy))
        return image
        