from collections import defaultdict
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        adj=defaultdict(list)
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        comp=0
        q=deque()
        visit=set()
        for i in range(n):
            if i not in visit:
                comp+=1
                q.append(i)
                visit.add(i)
                while q:
                    node=q.popleft()
                    
                    for neigh in adj[node]:
                        if neigh not in visit:
                            q.append(neigh)
                            visit.add(neigh)
        return comp-1


        
        