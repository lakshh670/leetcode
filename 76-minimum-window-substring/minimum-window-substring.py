class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count,s_count=defaultdict(int),defaultdict(int)
        for x in t:
            t_count[x]+=1
        for x in s:
            if x in t_count:
                s_count[x]+=1
        for x in t:
            if x not in s_count or s_count[x]<t_count[x]:
                return ""
        s_count=defaultdict(int)
        need,have=len(t_count),0
        x,y=0,len(s)-1
        l,r=0,0
        while r<len(s):
            if s[r] in t:
                s_count[s[r]]+=1
                if s_count[s[r]]==t_count[s[r]]:
                    have+=1
                    while have==need:
                        if s[l] in t:
                            s_count[s[l]]-=1
                            if s_count[s[l]]<t_count[s[l]]:
                                have-=1
                        if r-l <y-x:
                            x,y=l,r
                        l+=1
            r+=1
        return s[x:y+1]
        
        