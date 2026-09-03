class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cnt=0
        i,j=0,0
        g.sort()
        s.sort()
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                cnt+=1
                i+=1
                
            j+=1
        return cnt
        