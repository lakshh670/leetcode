class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        parent=[i for i in range(n)]
        rank=[1]*n
        def find_ulp(x):
            if parent[x]==x:
                return x
            parent[x]=find_ulp(parent[x])
            return parent[x]
        def union(x,y):
            ulp_x=find_ulp(x)
            ulp_y=find_ulp(y)
            if ulp_x!=ulp_y:
                if rank[ulp_x]>rank[ulp_y]:
                    parent[ulp_y]=ulp_x
                elif rank[ulp_x]<rank[ulp_y]:
                    parent[ulp_x]=ulp_y
                else:
                    parent[ulp_x]=ulp_y
                    rank[ulp_y]+=1
        for u in range(n):
            for v in range(u+1,n):
                if isConnected[u][v]:
                    union(u,v)
        s=set()
        
        for x in range(n):
            s.add(find_ulp(x))
        print(s)
        return len(s)
        