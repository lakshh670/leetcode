class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        n=len(word)
        row,col=len(board),len(board[0])
        def search(x,y,i):
            if i==n-1:
                return True
            visit.add((x,y))
            for dx,dy in [(-1,0),(0,-1),(0,1),(1,0)]:
                if 0<=x+dx<row and 0<=y+dy<col and (x+dx,y+dy) not in visit and board[x+dx][y+dy]==word[i+1]:
                    if search(x+dx,y+dy,i+1):
                        return True
            visit.remove((x,y))
            return False
        start=[]
        for i in range(row):
            for j in range(col):
                if board[i][j]==word[0]:
                    start.append((i,j))
        
        for x,y in start:
            visit=set()
            if search(x,y,0):
                return True
        return False
        