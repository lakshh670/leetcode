import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj=defaultdict(list)
        for u,v,w in roads:
            adj[u].append((v,w))
            adj[v].append((u,w))
        dist=[float('inf')]*n
        dist[0]=0
        q=[(0,0)]
        heapq.heapify(q)
        num_ways=[0]*n
        num_ways[0]=1
        MOD=10**9+7
        while q:
            dis,node=heapq.heappop(q)
            for neigh,wt in adj[node]:
                if dis+wt<dist[neigh]:
                    dist[neigh]=dis+wt
                    heapq.heappush(q,(dist[neigh],neigh))
                    num_ways[neigh]=num_ways[node]
                elif dis+wt==dist[neigh]:
                    num_ways[neigh]=(num_ways[node]+num_ways[neigh])%MOD
        return num_ways[n-1]


        