class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        par,size={},{}
        for x in nums:
            par[x]=x
            size[x]=1
        def find_par(x):
            if par[x]==x:
                return x
            par[x]=find_par(par[x])
            return par[x]
        def union(u,v):
            ulp_u=find_par(u)
            ulp_v=find_par(v)
            if ulp_u==ulp_v:
                return
            if size[ulp_u]<size[ulp_v]:
                par[ulp_u]=ulp_v
                size[ulp_v]+=size[ulp_u]
            else:
                par[ulp_v]=ulp_u
                size[ulp_u]+=size[ulp_v]
        s=set(nums)
        for x in s:
            if x-1 in par :
                union(x,x-1)
            elif x+1 in par:
                union(x,x+1)
        return max(size.values()) if size else 0

        