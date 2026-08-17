class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=[i for i in range(n+1)]
        rank=[1]*(n+1)
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
        ans=[]
        for u,v in edges:
            if find_ulp(u)==find_ulp(v):
                ans=[u,v]
            union(u,v)
        return ans
        