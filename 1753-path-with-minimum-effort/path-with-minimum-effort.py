class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # A common question is why this cannot be solved using Dynamic Programming.

        # Suppose we define a DP state:

        # dp(row, col) = minimum effort required to reach (row, col)
        # The problem is that to compute dp(row, col), you may come from:

        # Up
        # Down
        # Left
        # Right
        # So,

        # dp(row, col)
        #     depends on
        # dp(row-1,col)
        # dp(row+1,col)
        # dp(row,col-1)
        # dp(row,col+1)
        # But those neighboring states also depend on dp(row, col).

        # This creates a circular dependency, meaning there is no valid order in which the DP states can be computed.

        # Unlike classic grid DP problems (Unique Paths, Minimum Path Sum, etc.), movement is allowed in all four directions, creating cycles in the state graph.

        # DP works well when movement is restricted to directions like Right and Down, because there are no cycles and each state depends only on previously computed states.

        # Here, the grid behaves like a graph, not a DAG.

        # Therefore, this is fundamentally a shortest path problem, making Dijkstra's algorithm the appropriate solution.
        q=[(0,0,0)]
        heapq.heapify(q)
        m,n=len(heights),len(heights[0])
        visit=set()
        while q:
            curr_eff,x,y=heapq.heappop(q)
            if (x,y)==(m-1,n-1):
                return curr_eff
            if (x,y) in visit:
                continue
            visit.add((x,y))
            for dx,dy in [(1,0),(0,1),(0,-1),(-1,0)]:
                if 0<=x+dx<m and 0<=y+dy<n:
                    new_eff=max(abs(heights[x][y]-heights[x+dx][y+dy]),curr_eff)
                    heapq.heappush(q,(new_eff,x+dx,y+dy))
        
        