class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        import heapq
import sys
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}
        for i, j, cost in flights:
            if i not in adj:
                adj[i] = []
            adj[i].append((j, cost))

        # Priority Queue: (cost_so_far, current_node, steps_used)
        pq = deque()
        pq.append((0,src,0))

        dist=[sys.maxsize]*n
        dist[src]=0
        while pq:
            dis,node,steps=pq.popleft()
            if steps>k  : # No. of stops in a path=no. of edges in that path-1
                continue
            if node in adj:
                for neigh,ed_we in adj[node]:
                    if dis+ed_we<dist[neigh]:
                        dist[neigh]=dis+ed_we
                        pq.append((dist[neigh],neigh,steps+1))
        return dist[dst] if dist[dst]!=sys.maxsize else -1
        