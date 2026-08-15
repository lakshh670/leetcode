import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))
        q=[]
        heapq.heappush(q,(0,k))
        dist=[float('inf')]*(n+1)
        dist[k]=0
        
        while q:
            dis,node=heapq.heappop(q)
            if dis>dist[node]:
                continue
            for neigh,wt in adj[node]:

                
                if dis+wt<dist[neigh]:
                    
                    dist[neigh]=dis+wt
                    heapq.heappush(q,(dist[neigh],neigh))
        
        return max(dist[1:]) if max(dist[1:])!=float('inf') else -1

