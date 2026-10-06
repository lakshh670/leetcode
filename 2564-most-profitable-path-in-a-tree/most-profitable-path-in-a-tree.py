class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        bobs_time={}
        def dfs(src,par,time): # For bob
            if src==0:
                bobs_time[0]=time
                return True
            for neigh in adj[src]:
                if neigh==par:
                    continue
                if dfs(neigh,src,time+1):
                    bobs_time[src]=time
                    return True
            return False
        
        dfs(bob,-1,0)

        res=float('-inf')
        q=deque()
        q.append((0,-1,amount[0],0))
        while q:
            (node,par,profit,time)=q.popleft()
            for neigh in adj[node]:
                if neigh==par:
                    continue
                neigh_profit=amount[neigh]
                neigh_time=time+1
                if neigh in bobs_time:
                    if neigh_time>bobs_time[neigh]:
                        neigh_profit=0
                    elif neigh_time==bobs_time[neigh]:
                        neigh_profit=neigh_profit//2
                q.append((neigh,node,profit+neigh_profit,neigh_time))
                if len(adj[neigh])==1:
                    res=max(res,profit+neigh_profit)


        return res
        
        